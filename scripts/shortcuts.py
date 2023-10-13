import tkinter as tk

from PIL import ImageTk, Image

import scripts.schermen as schermen_class


# Maakt foto element aan en geeft terug
def maak_foto_label(foto_locatie: str, size: list, venster) -> tk.Label:
    image = Image.open(foto_locatie)
    image = image.resize((int(size[0]), int(size[1])))
    image = ImageTk.PhotoImage(image)
    label = tk.Label(venster, image=image)
    label.image = image

    return label


def bekijk_of_bestand_bestaat(bestandslocatie: str) -> bool:
    try:
        open(bestandslocatie)
        return True
    except FileNotFoundError:
        return False


def maak_frame(venster, config={}, grid={}) -> tk.Frame:
    frame = tk.Frame(venster)
    frame.config(config)

    if len(grid) > 0:
        frame.grid(grid)

    return frame


def maak_knop(venster, label, functie):
    start_button = tk.Button(venster, text=label,
                             command=functie)
    start_button.config(knop_stijl())

    return start_button


def maak_foto_klikbaar(label, venster, functie):
    label.bind("<Button-1>", lambda e: schermen_class.laad_scherm(functie, venster))


def maak_label(venster, label, config={}):
    title = tk.Label(venster, text=label)
    title.config(config)

    return title


def knop_stijl() -> dict:
    button_style = {
        "font": ("Ringbearer", 14),
        "bg": "white",
        "fg": "black",
        "activebackground": "black",
        "activeforeground": "white",
        "relief": "flat",
        "borderwidth": 0,
        "highlightthickness": 0,
        "cursor": "hand2",
        "padx": 10,
        "pady": 5,
    }

    return button_style
