import tkinter as tk
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts


# Niet de functienaam aanpassen, wordt automatisch ingeladen
def laad_scherm(venster: tk.Tk) -> None:
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Content
    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 "Gefeliciteerd! U heeft het spel uitgespeeld!",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()

    # Footer
    # frame
    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    # frame
    footer_frame_left = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_left.pack(side="left")

    # knop
    instellings_knop = shortcuts.maak_knop(footer_frame_left, "◄  Keer terug naar hoofdmenu",
                                           lambda: schermen_class.laad_scherm("start", venster))
    instellings_knop.pack(side="bottom", anchor="se", padx=10, pady=10)
