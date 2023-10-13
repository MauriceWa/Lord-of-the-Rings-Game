import tkinter as tk
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts
import scripts.locaties as locaties_class
import scripts.speler as speler_class
import scripts.npcs as npc_class


#   Niet de functienaam aanpassen, wordt automatisch ingeladen


def laad_scherm(venster: tk.Tk) -> None:
    # BEGIN header
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    speler = speler_class.verkrijg_speler()
    npc = locaties_class.verkrijg_npc_bij_id(speler["locatie_id"])

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # BEGIN titel
    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 f"U komt {npc['naam']} tegen",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 12})
    title.pack()

    # EIND titel & header

    # BEGIN content
    omschrijving_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    omschrijving_container.pack(side="top", fill="x")

    # Label
    omschrijving = shortcuts.maak_label(title_container,
                                        f"{npc['vraag']}",
                                        {"font": ("Ringbearer", 13), "bg": "#181818", "fg": "white", "pady": 10})
    omschrijving.pack()

    npc_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    npc_container.pack(pady=30)

    button_container = shortcuts.maak_frame(npc_container, {"bg": "#181818"})
    button_container.pack(pady=15)

    # Knop frame
    ja_frame = shortcuts.maak_frame(button_container,
                                    {"bg": "#181818"},
                                    {"row": 0, "column": 0, "sticky": "nsew", "padx": 10})

    # button
    ja_button = shortcuts.maak_knop(ja_frame,
                                    "Ja",
                                    lambda: ja_knop(venster))

    ja_button.pack()

    nee_frame = shortcuts.maak_frame(button_container,
                                     {"bg": "#181818"},
                                     {"row": 0, "column": 2, "sticky": "nsew", "padx": 10})

    nee_button = shortcuts.maak_knop(nee_frame,
                                     "Nee",
                                     lambda: nee_knop(venster))
    nee_button.pack()

    nee_button.pack(side="right")

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


def ja_knop(venster):
    npc_class.valideer_npc(venster, True)
    schermen_class.laad_scherm("keuze_locaties", venster)


def nee_knop(venster):
    schermen_class.laad_scherm("start", venster)
