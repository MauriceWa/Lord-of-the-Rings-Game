import scripts.speler as speler_class
import scripts.schermen as schermen_class
import json

def verkrijg_npc_bij_id(locatie_id):
    bestandslocatie = "data/npc.json"

    with open(bestandslocatie, "r") as bestand:
        npcs = json.load(bestand)

    for npc in npcs:
        if npc["locatie_id"] == locatie_id:
            return npc

def valideer_npc(venster, toestemming=False):
    speler = speler_class.verkrijg_speler()
    npc = verkrijg_npc_bij_id(speler["locatie_id"])

    # Kijk of er een NPC is gevonden op die locatie
    if not npc:
        return False

    # Voorkom dat speler al deze npc heeft
    if (isinstance(speler["npcs"], list)) and npc["id"] in speler["npcs"]:
        print("NPC is al behaald")
        return True

    # Kijk of er een vraag is, zo ja, laad het scherm
    elif npc["vraag"] and not toestemming:
        print("NPC heeft vraag")
        schermen_class.laad_scherm("npc_interactie", venster)
        return False

    # Kijk of er een behaal voorwaarde is, zo ja, valideer het
    elif (not isinstance(npc["behaal_voorwaarden"], list)) or check_npc_voorwaarden(npc["behaal_voorwaarden"]):
        if npc["geef_item"]:
            for item_id in npc["geef_item"]:
                speler_class.geef_item(item_id)
                print("NPC geeft item")

        speler_class.geef_npc(npc["id"])
        print("NPC behaald voorwaarden")
        return True

    # Kijk of er een ontsnap voorwaarde is, zo ja, valideer het
    if (not isinstance(npc["ontsnap_voorwaarden"], list)) or check_npc_voorwaarden(npc["ontsnap_voorwaarden"]):
        print("NPC ontsnapt voorwaarden")
        speler_class.update_speler_locatie(npc["vorige_locatie_id"])
        schermen_class.laad_scherm("speler_ontsnapt", venster)

    else:
        if npc["kan_dood"]:
            speler_class.maak_speler_aan()
            schermen_class.laad_scherm("dood", venster)
        else:
            speler_class.update_speler_locatie(npc["vorige_locatie_id"])
            schermen_class.laad_scherm("speler_loopt_vast", venster)
            return False


def check_npc_voorwaarden(voorwaardes):
    voldoet_aan_voorwaarden = False
    speler = speler_class.verkrijg_speler()

    for voorwaarde in voorwaardes:
        voorwaarde_list = voorwaarde.split(".")

        # Voorwaarde list [0] = key
        # Voorwaarde list [1] = value

        match voorwaarde_list[0]:
            case "npc":
                if not isinstance(speler["npcs"], list):
                    speler["npcs"] = []

                if int(voorwaarde_list[1]) in speler["npcs"]:
                    voldoet_aan_voorwaarden = True

            case "karakter":
                if int(speler["karakter_id"]) == int(voorwaarde_list[1]):
                    voldoet_aan_voorwaarden = True

            case "item":
                if not isinstance(speler["items"], list):
                    speler["items"] = []

                if int(voorwaarde_list[1]) in speler["items"]:
                    voldoet_aan_voorwaarden = True

    return voldoet_aan_voorwaarden
