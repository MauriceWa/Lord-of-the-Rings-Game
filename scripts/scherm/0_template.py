import tkinter as tk
from PIL import ImageTk, Image
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts


# Niet de functienaam aanpassen, wordt automatisch ingeladen
def laad_scherm(venster: tk.Tk) -> None:
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_container = shortcuts.maak_frame(venster, {"pady": 20})
    title_container.pack()

    # Label
    title = shortcuts.maak_label(title_container,
                                 "The Lord of the Rings: The Game",
                                 {"font": ("Arial", 40), "bg": "#181818", "fg": "white"})
    title.pack()


    # Content



    # Footer

    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    footer_frame_left = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_left.pack(side="left")

    footer_frame_right = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_right.pack(side="right")
