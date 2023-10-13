import tkinter as tk
import scripts.schermen as schermen_class
import scripts.shortcuts as shortcuts


# Niet de functienaam aanpassen, wordt automatisch ingeladen
def laad_scherm(tekst, popup: tk.Tk, functie) -> None:

    # message
    message = shortcuts.maak_label(popup,
                                        tekst,
                                        {"font": ("Arial", 15), "bg": "#181818", "fg": "white"})

    message.pack()

    button_container = shortcuts.maak_frame(popup, {"bg": "#181818"})
    button_container.pack(pady=15)

    # Knop frame
    ja_frame = shortcuts.maak_frame(button_container,
                                        {"bg": "#181818"},
                                        {"row": 0, "column": 0, "sticky": "nsew", "padx": 10})

    # button
    ja_button = shortcuts.maak_knop(ja_frame,
                                        "Ja",
                                        functie)

    ja_button.pack()

    nee_frame = shortcuts.maak_frame(button_container,
                                      {"bg": "#181818"},
                                      {"row": 0, "column": 2, "sticky": "nsew", "padx": 10})

    nee_button = shortcuts.maak_knop(nee_frame,
                                      "Nee",
                                      lambda: popup.destroy())
    nee_button.pack()

    nee_button.pack(side="right")
