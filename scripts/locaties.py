import json
import scripts.speler as speler_class


def verkrijg_locaties() -> list:
    bestandslocatie = "data/locaties.json"

    with open(bestandslocatie, "r") as bestand:
        locaties = json.load(bestand)

    return locaties


def verkrijg_locatie_bij_id(locatie_id: int) -> dict:
    locaties = verkrijg_locaties()

    for locatie in locaties:
        if locatie["id"] == locatie_id:
            return locatie

    return {}


def verkrijg_locaties_ernaast(locatie_id: int) -> list:
    huidige_locatie = verkrijg_locatie_bij_id(locatie_id)
    alle_locaties = verkrijg_locaties()
    locaties_ernaast = []

    for locatie in alle_locaties:
        if locatie['id'] in huidige_locatie["naast_locatie_ids"]:
            locaties_ernaast.append(locatie)

    return locaties_ernaast

def verkrijg_start_locaties():
    locaties = verkrijg_locaties()
    eindlocaties = []

    for locatie in locaties:
        if locatie["start_locatie"]:
            eindlocaties.append(locatie)

    return eindlocaties


def verkrijg_npc_bij_id(locatie_id: int) -> dict:
    bestandslocatie = "data/npc.json"

    with open(bestandslocatie, "r") as bestand:
        npcs = json.load(bestand)

    for npc in npcs:
        if npc["locatie_id"] == locatie_id:
            return npc


def verkrijg_npc_bij_id(locatie_id: int) -> dict:
    bestandslocatie = "data/npc.json"

    with open(bestandslocatie, "r") as bestand:
        npcs = json.load(bestand)

    for npc in npcs:
        if npc["locatie_id"] == locatie_id:
            return npc


def mag_speler_locatie_zien(locatie_id: int) -> bool:
    locatie = verkrijg_locatie_bij_id(locatie_id)
    speler = speler_class.verkrijg_speler()
    speler_mag_door = True

    if (isinstance(locatie["toegang_voor"], list)) and len(locatie["toegang_voor"]) > 0:
        speler_mag_door = False

        for karakter_id in locatie["toegang_voor"]:
            if speler["karakter_id"] == karakter_id:
                speler_mag_door = True
                break

    if not speler_mag_door:
        return False

    return True
