import threading
import tkinter as tk
import scripts.shortcuts as shortcuts
import scripts.schermen as scherm_class
import scripts.instellingen as instellings_class


def laad_scherm(venster: tk.Tk) -> None:
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/splashscreen.png",
                                                 [1536, 836], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    # frame
    footer_frame_right = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_right.pack(side="right")

    # Start the function running asynchronously
    start_applicatie_na_3_seconden(venster)


def start_applicatie_na_3_seconden(venster):
    venster.after(3000, lambda: laad_start_scherm(venster))
    laad_achtergrond_muziek_in()


def laad_start_scherm(venster):
    scherm_class.laad_scherm("start", venster)


def laad_achtergrond_muziek_in():
    threading.Timer(3, instellings_class.verander_muziek, args=("achtergrond",)).start()
