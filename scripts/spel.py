import scripts.schermen as scherm_class
import scripts.instellingen as instellingen_class


def start():
    instellingen_class.start_muziek()

    spel_venster = scherm_class.maak_venster()

    scherm_class.laad_scherm("splashscreen", spel_venster)
