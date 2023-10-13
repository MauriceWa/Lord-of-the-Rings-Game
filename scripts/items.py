import scripts.speler as speler_class
import scripts.schermen as schermen_class
import scripts.locaties as locaties_class
import json


def verkrijg_items_bij_id():
    bestandslocatie = "data/items.json"
    speler = speler_class.verkrijg_speler()

    with open(bestandslocatie, "r") as bestand:
        items = json.load(bestand)

    speler_items = []

    for item in items:
        if item["id"] in speler["items"]:
            speler_items.append(item)

    return speler_items

def valideer_geef_items():
    speler = speler_class.verkrijg_speler()
    locatie = locaties_class.verkrijg_locatie_bij_id(speler["locatie_id"])

    if (isinstance(locatie["item_id"], list)) and len(locatie["item_id"]) > 0:
        for item in locatie["item_id"]:
            if item not in speler["items"]:
                print(f"Item {item} gevonden")
                speler_class.geef_item(item)

            else:
                print(f"Item {item} is al gevonden")


def valideer_items(locatie_id, venster):
    locatie = locaties_class.verkrijg_locatie_bij_id(locatie_id)
    speler_mag_door = True

    if (isinstance(locatie["benodigde_items"], list)) and len(locatie["benodigde_items"]) > 0:
        speler_mag_door = False

        for item in locatie["benodigde_items"]:
            if speler_class.heeft_item(item):
                speler_mag_door = True
                break

    if not speler_mag_door:
        return False

    return True

