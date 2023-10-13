import tkinter as tk
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts
import scripts.speler as speler_class

# Niet de functienaam aanpassen, wordt automatisch ingeladen
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
                                 "Kies het geslacht",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()


    # Content

    # Button container
    knop_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    knop_container.pack(pady=30)

    # Knop frame
    button_frame = shortcuts.maak_frame(knop_container,
                                        {"bg": "#181818"},
                                        {"row": 0, "column": 0, "sticky": "nsew", "padx": 10, "pady": 10})

    # Image label
    image_label = shortcuts.maak_foto_label("assets/afbeeldingen/man.png",
                                            [300, 230], button_frame)
    image_label.config(highlightthickness=0, relief='ridge', bd=0)
    image_label.bind("<Button-1>", lambda e: speler_gender("man", venster))
    image_label.pack()

    # Knop
    start_button = shortcuts.maak_knop(button_frame,
                                       "Man",
                                       lambda: speler_gender("man", venster))
    start_button.pack(pady=5)

    # Frame
    stop_frame = shortcuts.maak_frame(knop_container,
                                        {"bg": "#181818"},
                                        {"row": 0, "column": 1, "sticky": "nsew", "padx": 10, "pady": 15})

    # Foto
    image_label = shortcuts.maak_foto_label("assets/afbeeldingen/vrouw.png",
                                            [300, 230], stop_frame)
    image_label.config(highlightthickness=0, relief='ridge', bd=0)
    image_label.bind("<Button-1>", lambda e: speler_gender("vrouw", venster))
    image_label.pack()

    quit_button = shortcuts.maak_knop(stop_frame,
                                      "Vrouw",
                                      lambda: speler_gender("vrouw", venster))
    quit_button.pack(pady=5)

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


def speler_gender(gender, venster):
    speler_class.update_speler_gender(gender)
    schermen_class.laad_scherm(f"karakter_{gender}", venster)
