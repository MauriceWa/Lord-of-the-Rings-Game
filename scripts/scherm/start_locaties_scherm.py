import tkinter as tk
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts
import scripts.locaties as locaties_class
import scripts.speler as speler_class


def laad_scherm(venster: tk.Tk) -> None:
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 "Kies een startlocatie",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()

    start_locaties = locaties_class.verkrijg_start_locaties()
    start_locatie_nummer = 0

    knop_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    knop_container.pack(pady=30)
    start_locatie_frame = {}
    start_locatie_label = {}
    keuze_nummer = 0


    for start_locatie in start_locaties:
        start_locatie_frame[keuze_nummer] = shortcuts.maak_frame(knop_container,
                                                         {"bg": "#181818"},
                                                         {"row": 0, "column": start_locatie_nummer, "sticky": "nsew",
                                                          "padx": 10, "pady": 10}
                                                         )

        # Selecteer de juiste afbeelding als hij bestaat, zo niet gebruik grot.png
        if shortcuts.bekijk_of_bestand_bestaat(f"assets/afbeeldingen/locaties/{start_locatie['id']}.png"):
            start_locatie_label[keuze_nummer] = shortcuts.maak_foto_label(
                f"assets/afbeeldingen/locaties/{start_locatie['id']}.png", [300, 224],
                start_locatie_frame[keuze_nummer])
        else:
            start_locatie_label[keuze_nummer] = shortcuts.maak_foto_label("assets/afbeeldingen/grot.png", [300, 224],
                                                                  start_locatie_frame[keuze_nummer])

        start_locatie_label[keuze_nummer].config(highlightthickness=0, relief='ridge', bd=0)
        start_locatie_label[keuze_nummer].place(x=10, y=10, relwidth=1, relheight=1)
        start_locatie_label[keuze_nummer].bind("<Button-1>",
                                       lambda e,kn=start_locatie['id']: verander_speler_locatie(kn, venster))
        start_locatie_label[keuze_nummer].pack()

        if start_locatie['eind_locatie'] is True and start_locatie['goed_einde'] is True:
            shortcuts.maak_knop(start_locatie_frame[keuze_nummer],
                                start_locatie['naam'],
                                lambda: schermen_class.laad_scherm("goed_einde", venster)).pack(pady=5)

        elif start_locatie['eind_locatie'] is True and start_locatie['goed_einde'] is False:
            shortcuts.maak_knop(start_locatie_frame[keuze_nummer],
                                start_locatie['naam'],
                                lambda: schermen_class.laad_scherm("slecht_einde", venster)).pack(pady=5)

        else:
            shortcuts.maak_knop(start_locatie_frame[keuze_nummer],
                                start_locatie['naam'],
                                lambda kn=start_locatie['id']: verander_speler_locatie(kn, venster)).pack(pady=5)

        start_locatie_nummer += 1


    # Footer
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