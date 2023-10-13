import tkinter as tk
import scripts.schermen as schermen_class
import scripts.locaties as locaties_class
import scripts.shortcuts as shortcuts


# Niet de functienaam aanpassen, wordt automatisch ingeladen
def laad_scherm(venster: tk.Tk) -> None:
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # BEGIN titel
    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 "Beheerdersscherm",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()

    # EIND titel

    # BEGIN content

    # Locaties container
    locatie_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    locatie_container.pack(pady=30)

    canvas = tk.Canvas(locatie_container, width=1250, height=500)
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

    locatie_nummer = 0
    locaties = locaties_class.verkrijg_locaties()

    # Locatie ID frame
    locatie_id_frame = shortcuts.maak_frame(content_frame,
                                            {"bg": "#181818"},
                                            {"row": locatie_nummer, "column": 0, "sticky": "nsew",
                                             "padx": 10, "pady": 10})

    # Text label
    locatie_id_label = shortcuts.maak_label(locatie_id_frame,
                                            "ID",
                                            {"bg": "#181818", "fg": "white", "pady": 5, "font": ("Ringbearer", 15)})
    locatie_id_label.pack()

    # Locatie naam frame
    locatie_naam_frame = shortcuts.maak_frame(content_frame,
                                              {"bg": "#181818"},
                                              {"row": locatie_nummer, "column": 1, "sticky": "nsew",
                                               "padx": 10, "pady": 10})

    # Text label
    locatie_naam_label = shortcuts.maak_label(locatie_naam_frame,
                                              "Naam",
                                              {"bg": "#181818", "fg": "white", "pady": 5,
                                               "font": ("Ringbearer", 15)})
    locatie_naam_label.pack()

    # Locatie nummer frame
    optie1_naam_label = shortcuts.maak_frame(content_frame,
                                             {"bg": "#181818"},
                                             {"row": locatie_nummer, "column": 2, "sticky": "nsew",
                                              "padx": 10, "pady": 10})

    # Optie 1 label
    optie1_naam_label = shortcuts.maak_label(optie1_naam_label,
                                             "Optie 1",
                                             {"bg": "#181818", "fg": "white", "pady": 5,
                                              "font": ("Ringbearer", 15)})
    optie1_naam_label.pack()

    # Optie 2 frame
    optie2_naam_frame = shortcuts.maak_frame(content_frame,
                                             {"bg": "#181818"},
                                             {"row": locatie_nummer, "column": 3, "sticky": "nsew",
                                              "padx": 10, "pady": 10})

    # Text label
    optie2_naam_label = shortcuts.maak_label(optie2_naam_frame,
                                             "Optie 2",
                                             {"bg": "#181818", "fg": "white", "pady": 5,
                                              "font": ("Ringbearer", 15)})
    optie2_naam_label.pack()

    # Optie 3 frame
    optie3_naam_frame = shortcuts.maak_frame(content_frame,
                                             {"bg": "#181818"},
                                             {"row": locatie_nummer, "column": 4, "sticky": "nsew",
                                              "padx": 10, "pady": 10})

    # Text label
    optie3_naam_label = shortcuts.maak_label(optie3_naam_frame,
                                             "Locatie 3",
                                             {"bg": "#181818", "fg": "white", "pady": 5,
                                              "font": ("Ringbearer", 15)})
    optie3_naam_label.pack()

    locatie_nummer += 1

    for locatie in locaties:
        kolom_id = 0

        # Locatie naam frame
        locatie_id_frame = shortcuts.maak_frame(content_frame,
                                                {"bg": "#181818"},
                                                {"row": locatie_nummer, "column": kolom_id, "sticky": "nsew",
                                                 "padx": 10, "pady": 10})

        # Text label
        locatie_id_label = shortcuts.maak_label(locatie_id_frame,
                                                locatie['id'],
                                                {"bg": "#181818", "fg": "white", "pady": 5, "font": ("Ringbearer", 15)})
        locatie_id_label.pack()

        kolom_id += 1

        # Locatie naam frame
        locatie_naam_frame = shortcuts.maak_frame(content_frame,
                                                  {"bg": "#181818"},
                                                  {"row": locatie_nummer, "column": kolom_id, "sticky": "nsew",
                                                   "padx": 10, "pady": 10})

        # Text label
        locatie_naam_label = shortcuts.maak_label(locatie_naam_frame,
                                                  locatie['naam'],
                                                  {"bg": "#181818", "fg": "white", "pady": 5,
                                                   "font": ("Ringbearer", 15)})
        locatie_naam_label.pack()

        kolom_id += 1

        for optie in locatie['naast_locatie_ids']:
            optie_locatie = locaties_class.verkrijg_locatie_bij_id(optie)

            if len(optie_locatie) == 0:
                continue

            # Locatie stappen frame
            locatie_stappen_frame = shortcuts.maak_frame(content_frame,
                                                         {"bg": "#181818"},
                                                         {"row": locatie_nummer, "column": kolom_id, "sticky": "nsew",
                                                          "padx": 10, "pady": 10})

            # Text label
            locatie_stappen_label = shortcuts.maak_label(locatie_stappen_frame,
                                                         optie_locatie['naam'],
                                                         {"bg": "#181818", "fg": "white", "pady": 5,
                                                          "font": ("Ringbearer", 15)})
            locatie_stappen_label.pack()

            kolom_id += 1

        locatie_nummer += 1

    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Footer
    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    footer_frame_left = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_left.pack(side="left")

    terug_knop = shortcuts.maak_knop(footer_frame_left, "◄  Keer terug naar de instellingen",
                                     lambda: schermen_class.laad_scherm("instellingen", venster))
    terug_knop.pack(side="bottom", anchor="se", padx=10, pady=10)
