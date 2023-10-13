import tkinter as tk
import scripts.schermen as schermen_class
import scripts.instellingen as instellingen_class
import scripts.shortcuts as shortcuts


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
                                 "Instellingen",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()

    button_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    button_container.pack(pady=30)

    frame = shortcuts.maak_frame(button_container,
                                 {"bg": "#181818"},
                                 {"row": 0, "column": 0, "sticky": "nsew", "padx": 10, "pady": 10}
                                 )

    muziek_label = shortcuts.maak_foto_label("assets/afbeeldingen/muziek.jpg",
                                             [300, 230], frame)
    muziek_label.config(highlightthickness=0, relief='ridge', bd=0)
    muziek_label.bind("<Button-1>", lambda e: instellingen_class.easter_egg_muziek())
    muziek_label.pack(pady=5)

    if instellingen_class.verkrijg_muziek_status():
        muziek_button_label = "⏸  Pauzeren"
    else:
        muziek_button_label = "▶  Hervatten"

    muziek_button = shortcuts.maak_knop(frame, muziek_button_label, lambda: toggle_muziek(muziek_button))
    muziek_button.pack()

    volume_slider = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=instellingen_class.verander_volume)
    volume_slider.set(instellingen_class.verkrijg_volume())
    volume_slider.pack()

    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    footer_frame_left = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_left.pack(side="left")

    footer_frame_right = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_right.pack(side="right")

    terug_knop = shortcuts.maak_knop(footer_frame_left, "◄  Keer terug naar hoofdmenu",
                                     lambda: schermen_class.laad_scherm("start", venster))
    terug_knop.pack(side="bottom", anchor="se", padx=10, pady=10)

    beheerders_knop = shortcuts.maak_knop(footer_frame_right, "Beheerderspaneel",
                                          lambda: schermen_class.laad_scherm("inlog", venster))
    beheerders_knop.pack(side="bottom", anchor="se", padx=10, pady=10)


def toggle_muziek(button: tk.Button) -> None:
    muziek_status = instellingen_class.verkrijg_muziek_status()

    if muziek_status:
        instellingen_class.pauzeer_muziek()
        button.config(text="▶  Hervatten")

    else:
        instellingen_class.hervat_muziek()
        button.config(text="⏸  Pauzeren")
