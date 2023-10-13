import json


def verkrijg_karakters() -> list:
    bestandslocatie = "data/karakters_vrouw.json"

    with open(bestandslocatie, "r") as bestand:
        karakters = json.load(bestand)

    return karakters


def verkrijg_karakter_bij_id(karakter_id: int) -> dict:
    karakters = verkrijg_karakters()

    for karakter in karakters:
        if karakter["id"] == karakter_id:
            return karakter

    return {}
