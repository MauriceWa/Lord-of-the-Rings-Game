import tkinter as tk
import scripts.schermen as schermen_class
import bcrypt
import scripts.shortcuts as shortcuts

WACHTWOORD_HASH = "$2a$12$JyhZCCsIjsYFp9ExxRGgjepxX4mL1Qr5CkcmHopLkSyjKSKp7cMJO".encode('utf-8')


# Niet de functienaam aanpassen, wordt automatisch ingeladen
def laad_scherm(venster: tk.Tk) -> None:
    veld_stijl = {
        "bg": "#3d3d3d",
        "fg": "white",
        "relief": "flat",
        "borderwidth": 0,
        "highlightthickness": 0,
    }
    window_width = venster.winfo_screenwidth()
    window_height = venster.winfo_screenheight()

    background_label = shortcuts.maak_foto_label("assets/afbeeldingen/achtergrond.png",
                                                 [window_width, window_height], venster)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    title_container.pack(side="top", fill="x")

    # Label
    title = shortcuts.maak_label(title_container,
                                 "Inloggen in beheerderspaneel",
                                 {"font": ("Ringbearer", 25), "bg": "#181818", "fg": "white", "pady": 20})
    title.pack()

    inlog_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    inlog_container.pack(pady=30, ipady=10, ipadx=10)

    wachtwoord_label = shortcuts.maak_label(inlog_container,
                                            "Voer het wachtwoord in",
                                            {"bg": "#181818", "pady": 10, "fg": "white", "font": ("Arial", 12)})
    wachtwoord_label.pack()

    wachtwoord_veld = tk.Entry(inlog_container)
    wachtwoord_veld.config(veld_stijl)
    wachtwoord_veld.pack(side=tk.TOP, ipadx=30, ipady=10)

    bericht_veld = shortcuts.maak_label(venster, "")

    login_knop = shortcuts.maak_knop(inlog_container, "Inloggen", lambda: valideer_input(wachtwoord_veld,
                                                                                         bericht_veld, venster))
    login_knop.pack(pady=7)

    # Footer
    footer_container = shortcuts.maak_frame(venster, {"bg": "#181818"})
    footer_container.pack(side="bottom", fill="x")

    footer_frame_left = shortcuts.maak_frame(footer_container, {"bg": "#181818"})
    footer_frame_left.pack(side="left")

    terug_knop = shortcuts.maak_knop(footer_frame_left, "◄  Keer terug naar de instellingen",
                                     lambda: schermen_class.laad_scherm("instellingen", venster))
    terug_knop.pack(side="bottom", anchor="se", padx=10, pady=10)


def valideer_input(wachtwoord_veld, bericht_veld, venster):
    wachtwoord = wachtwoord_veld.get()

    password_correct = bcrypt.checkpw(wachtwoord.encode('utf-8'), WACHTWOORD_HASH)

    if password_correct:
        schermen_class.laad_scherm("beheerder", venster)
    else:
        bericht_veld.config(text="Uw wachtwoord is onjuist")
        bericht_veld.pack(side=tk.TOP, ipadx=30, ipady=10)
