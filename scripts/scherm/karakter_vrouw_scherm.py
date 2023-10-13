import tkinter as tk
import scripts.schermen as schermen_class
import scripts.karakters_vrouw as karakter_class
import scripts.shortcuts as shortcuts
import scripts.speler as speler_class


# Niet de functienaam aanpassen, wordt automatisch ingeladen
def laad_scherm(venster: tk.Tk) -> None:
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.jpg",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 "Karakter selectie",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 10})
    title.pack()

    omschrijving_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    omschrijving_container.pack(side="top", fill="x")

    # Label
    omschrijving = shortcuts.maak_label(title_container,
                                 f"Denk goed na over je keuze, want dit heeft invloed op waar je komen in het verhaal.",
                                 {"font": ("Ringbearer", 13), "bg": "#181818", "fg": "white", "pady": 10})
    omschrijving.pack()

    # Content

    # frame
    locatie_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    locatie_container.pack(pady=30)

    canvas = tk.Canvas(locatie_container, width=1000, height=500)
    canvas.config(bg="#181818", highlightthickness=0, relief='ridge', bd=0)
    canvas.pack(side="left", fill="both", expand=True)

    # Create a Frame to serve as the content frame for your widgets
    content_frame = tk.Frame(canvas)
    content_frame.config(bg="#181818")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Create a vertical scrollbar and link it to the canvas and content frame
    scrollbar = tk.Scrollbar(locatie_container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    karakters = karakter_class.verkrijg_karakters()
    karakter_nummer = 0
    rij_nummer = 0

    for karakter in karakters:
        if karakter_nummer % 3 == 0:
            rij_nummer += 1
            karakter_nummer = 0

        optie_frame = shortcuts.maak_frame(content_frame,
                                           {"bg": "#181818"},
                                           {"row": rij_nummer, "column": karakter_nummer, "sticky": "nsew",
                                            "padx": 10, "pady": 10}
                                           )

        # Selecteer de juiste afbeelding als hij bestaat, zo niet gebruik grot.png
        if shortcuts.bekijk_of_bestand_bestaat(f"assets/afbeeldingen/{karakter['img_src']}"):
            optie_label = shortcuts.maak_foto_label(
                f"assets/afbeeldingen/{karakter['img_src']}", [300, 224],
                optie_frame)
        else:
            optie_label = shortcuts.maak_foto_label("assets/afbeeldingen/grot.png", [300, 224],
                                                    optie_frame)

        optie_label.config(highlightthickness=0, relief='ridge', bd=0)
        optie_label.place(x=10, y=10, relwidth=1, relheight=1)
        optie_label.bind("<Button-1>",
                         lambda e, kn=karakter['id']: verander_speler_karakter(kn, venster))
        optie_label.pack()

        shortcuts.maak_knop(optie_frame,
                            karakter['naam'],
                            lambda kn=karakter['id']: verander_speler_karakter(kn, venster)).pack(pady=5)

        karakter_nummer += 1

    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

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


def verander_speler_karakter(karakter, venster):
    speler_class.update_speler_karakter(karakter)
    schermen_class.laad_scherm("start_locaties", venster)
