import tkinter as tk
from PIL import ImageTk, Image
import sys


def maak_venster() -> tk.Tk:
    venster = tk.Tk()
    venster.title("Lord of the Rings: The Game")
    venster.wm_title = "Lord of the Rings: The Game"
    venster.geometry("1500x720")
    venster.resizable(True, True)

    icon = ImageTk.PhotoImage(Image.open("assets/afbeeldingen/logo.png"))
    venster.iconphoto(False, icon)

    return venster


def verwijder_elementen(venster: tk.Tk) -> None:
    for widget in venster.winfo_children():
        widget.destroy()


def laad_scherm(schermnaam: str, venster: tk.Tk) -> None:
    # pyglet.font.add_file('assets/lettertypen/ringbearer.ttf')
    verwijder_elementen(venster)

    scherm = __import__(f"scripts.scherm.{schermnaam}_scherm", fromlist=['laad_scherm'])
    scherm.laad_scherm(venster)

    del scherm
    sys.modules.pop(f"scripts.scherm.{schermnaam}_scherm")

    venster.mainloop()


def laad_popup(venster, titel: str, tekst: str, functie) -> None:
    popup = tk.Toplevel(venster)
    popup.title(titel)
    popup.wm_title = titel
    popup.geometry("400x150")
    popup.resizable(False, False)
    popup.config(bg="#181818")

    scherm = __import__(f"scripts.scherm.dialog_venster_scherm", fromlist=['laad_scherm'])
    scherm.laad_scherm(tekst, popup, functie)

    popup.mainloop()
