import scripts.schermen as schermen
import scripts.shortcuts as shortcuts
import scripts.speler as speler_class
import scripts.instellingen as instellings_class


# Niet de functienaam aanpassen, wordt automatisch ingeladen

def laad_scherm(venster):
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 "The Lord of the Rings: The Game",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()

    # Button container
    knop_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    knop_container.pack(pady=30)

    # Knop frame
    button_frame = shortcuts.maak_frame(knop_container,
                                        {"bg": "#181818"},
                                        {"row": 0, "column": 0, "sticky": "nsew", "padx": 10, "pady": 10})

    # Image label
    image_label = shortcuts.maak_foto_label("assets/afbeeldingen/start.png",
                                            [300, 230], button_frame)
    image_label.config(highlightthickness=0, relief='ridge', bd=0)

    if speler_class.verkrijg_speler()['locatie_id'] > 1:
        start_knop_label = "Nieuw spel"
        image_label.bind("<Button-1>", lambda e: schermen.laad_popup(venster, "Opnieuw beginnen",
                                               "Let op!\n"
                                               "Uw oude gegevens gaan verloren als u opnieuw begint.\n"
                                               "Weet u zeker dat u opnieuw wilt beginnen?",
                                           lambda: start_spel(venster)))
        # Knop
        start_button = shortcuts.maak_knop(button_frame,
                                           start_knop_label,
                                           lambda: schermen.laad_popup(venster, "Opnieuw beginnen",
                                               "Let op!\n"
                                               "Uw oude gegevens gaan verloren als u opnieuw begint.\n"
                                               "Weet u zeker dat u opnieuw wilt beginnen?",
                                           lambda: start_spel(venster)))
    else:
        start_knop_label = "Starten"
        image_label.bind("<Button-1>", lambda e: start_spel(venster))
        # Knop
        start_button = shortcuts.maak_knop(button_frame,
                                           start_knop_label,
                                           lambda: start_spel(venster))

    image_label.pack()
    start_button.pack(pady=5)

    if speler_class.verkrijg_speler()['locatie_id'] > 1:
        # Knop frame
        button_frame = shortcuts.maak_frame(knop_container,
                                            {"bg": "#181818"},
                                            {"row": 0, "column": 1, "sticky": "nsew", "padx": 10, "pady": 10})

        # Image label
        image_label = shortcuts.maak_foto_label("assets/afbeeldingen/hervatten.png",
                                                [300, 230], button_frame)
        image_label.config(highlightthickness=0, relief='ridge', bd=0)
        image_label.bind("<Button-1>", lambda e: schermen.laad_scherm("keuze_locaties", venster))
        image_label.pack()

        # Knop
        hervat_button = shortcuts.maak_knop(button_frame,
                                            "Spel hervatten",
                                            lambda: schermen.laad_scherm("keuze_locaties", venster))
        hervat_button.pack(pady=5)

    # Frame
    stop_frame = shortcuts.maak_frame(knop_container,
                                      {"bg": "#181818"},
                                      {"row": 0, "column": 2, "sticky": "nsew", "padx": 10, "pady": 10})

    # Foto
    image_label = shortcuts.maak_foto_label("assets/afbeeldingen/afsluiten.png",
                                            [300, 230], stop_frame)
    image_label.config(highlightthickness=0, relief='ridge', bd=0)
    image_label.bind("<Button-1>", lambda e: venster.destroy())
    image_label.pack()

    quit_button = shortcuts.maak_knop(stop_frame,
                                      "Afsluiten",
                                      lambda: venster.destroy())
    quit_button.pack(pady=5)

    # frame
    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    # frame
    footer_frame_right = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_right.pack(side="right")

    # knop
    instellings_knop = shortcuts.maak_knop(footer_frame_right, "Instellingen",
                                           lambda: schermen.laad_scherm("instellingen", venster))
    instellings_knop.pack(side="bottom", anchor="se", padx=10, pady=10)


def start_spel(venster) -> None:
    speler_class.maak_speler_aan()
    schermen.laad_scherm("man_of_vrouw_karakter", venster)
