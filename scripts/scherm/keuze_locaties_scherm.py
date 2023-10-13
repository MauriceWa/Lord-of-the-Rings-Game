import tkinter as tk
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts
import scripts.locaties as locaties_class
import scripts.speler as speler_class
import scripts.npcs as npcs_class
import scripts.items as items_class


#   Niet de functienaam aanpassen, wordt automatisch ingeladen


def laad_scherm(venster: tk.Tk) -> None:
    items_class.valideer_geef_items()

    # valideer of er een npc is
    npcs_class.valideer_npc(venster)

    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    speler = speler_class.verkrijg_speler()
    locatie_id = speler["locatie_id"]
    locatie = locaties_class.verkrijg_locatie_bij_id(locatie_id)

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # BEGIN titel
    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 f"U bevindt zich in: {locatie['naam']}",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 12})
    title.pack()

    # EIND titel

    # BEGIN content
    # frame
    # Text label
    omschrijving_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    omschrijving_container.pack(side="top", fill="x")

    # Label
    omschrijving = shortcuts.maak_label(title_container,
                                 f"{locatie['omschrijving']}",
                                 {"font": ("Ringbearer", 13), "bg": "#181818", "fg": "white", "pady": 10})
    omschrijving.pack()

    locatie_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    locatie_container.pack(pady=30)
    keuze_nummer = 0
    optie_label = {}
    optie_frame = {}

    for keuze in locatie['naast_locatie_ids']:
        locatie_ernaast = locaties_class.verkrijg_locatie_bij_id(keuze)

        if not items_class.valideer_items(locatie_ernaast['id'], venster):
            continue

        if not locaties_class.mag_speler_locatie_zien(locatie_ernaast['id']):
            continue


        optie_frame[keuze_nummer] = shortcuts.maak_frame(locatie_container,
                                                         {"bg": "#181818"},
                                                         {"row": 0, "column": keuze_nummer, "sticky": "nsew",
                                                          "padx": 10, "pady": 10}
                                                         )

        # Selecteer de juiste afbeelding als hij bestaat, zo niet gebruik grot.png
        if shortcuts.bekijk_of_bestand_bestaat(f"assets/afbeeldingen/locaties/{locatie_ernaast['id']}.png"):
            optie_label[keuze_nummer] = shortcuts.maak_foto_label(f"assets/afbeeldingen/locaties/{locatie_ernaast['id']}.png", [300, 224],
                                                              optie_frame[keuze_nummer])
        else:
            optie_label[keuze_nummer] = shortcuts.maak_foto_label("assets/afbeeldingen/grot.png", [300, 224],
                                                                optie_frame[keuze_nummer])

        optie_label[keuze_nummer].config(highlightthickness=0, relief='ridge', bd=0)
        optie_label[keuze_nummer].place(x=10, y=10, relwidth=1, relheight=1)
        optie_label[keuze_nummer].bind("<Button-1>",
                                       lambda e,kn=locatie_ernaast['id']: verander_speler_locatie(kn, venster))
        optie_label[keuze_nummer].pack()

        if locatie_ernaast['eind_locatie'] is True and locatie_ernaast['goed_einde'] is True:
            shortcuts.maak_knop(optie_frame[keuze_nummer],
                                locatie_ernaast['naam'],
                                lambda: schermen_class.laad_scherm("goed_einde", venster)).pack(pady=5)

        elif locatie_ernaast['eind_locatie'] is True and locatie_ernaast['goed_einde'] is False:
            shortcuts.maak_knop(optie_frame[keuze_nummer],
                                locatie_ernaast['naam'],
                                lambda: schermen_class.laad_scherm("slecht_einde", venster)).pack(pady=5)

        else:
            shortcuts.maak_knop(optie_frame[keuze_nummer],
                                locatie_ernaast['naam'],
                                lambda kn=locatie_ernaast['id']: verander_speler_locatie(kn, venster)).pack(pady=5)

        keuze_nummer += 1

    # Footer

    # frame
    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    # frame
    footer_frame_left = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_left.pack(side="left")

    terug_knop = shortcuts.maak_knop(footer_frame_left, "◄  Keer terug naar hoofdmenu",
                                     lambda: schermen_class.laad_scherm("start", venster))
    terug_knop.pack(side="bottom", anchor="se", padx=10, pady=10)


def verander_speler_locatie(locatie_ernaast, venster):
    speler_class.update_speler_locatie(locatie_ernaast)
    schermen_class.laad_scherm("keuze_locaties", venster)
