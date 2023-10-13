import json


def verkrijg_speler() -> list:
    bestandslocatie = "data/speler.json"

    with open(bestandslocatie, "r") as bestand:
        speler = json.load(bestand)

    return speler


def update_speler_locatie(locatie_id: int) -> None:
    speler = verkrijg_speler()
    speler["locatie_id"] = locatie_id

    with open("data/speler.json", "w") as bestand:
        json.dump(speler, bestand, indent=4)


def maak_speler_aan() -> None:
    # clear speler.json
    with open("data/speler.json", "w") as bestand:
        json.dump([], bestand, indent=4)

    speler = {
        "id": 1,
        "gender": "",
        "karakter_id": 1,
        "locatie_id": 1,
        "items": [],
        "npcs": []
    }

    with open("data/speler.json", "w") as bestand:
        json.dump(speler, bestand, indent=4)


def update_speler_gender(gender: str) -> None:
    speler = verkrijg_speler()
    speler['gender'] = gender

    # save player
    with open("data/speler.json", "w") as bestand:
        json.dump(speler, bestand, indent=4)


def update_speler_karakter(karakter_id) -> None:
    speler = verkrijg_speler()
    speler['karakter_id'] = karakter_id

    # save player
    with open("data/speler.json", "w") as bestand:
        json.dump(speler, bestand, indent=4)


def geef_item(item_id) -> None:
    speler = verkrijg_speler()

    if not isinstance(speler['items'], list):
        speler['items'] = []

    speler['items'].append(item_id)

    # save player
    with open("data/speler.json", "w") as bestand:
        json.dump(speler, bestand, indent=4)


def geef_npc(npc_id) -> None:
    speler = verkrijg_speler()

    if not isinstance(speler['npcs'], list):
        speler['npcs'] = []

    speler['npcs'].append(npc_id)

    # save player
    with open("data/speler.json", "w") as bestand:
        json.dump(speler, bestand, indent=4)


def heeft_item(item_id):
    speler = verkrijg_speler()

    if not isinstance(speler['items'], list):
        speler['items'] = []

    if item_id in speler['items']:
        return True

    return False
