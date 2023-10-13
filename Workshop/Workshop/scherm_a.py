from tkinter import Label, Button
from tkinter.font import Font

from Schoolopdrachten.Oefenen.Workshop.scherm_b import maak_scherm_b_aan

from PIL import Image, ImageTk


def maak_scherm_a_aan(venster):
    # scherm wissen
    for widget in venster.winfo_children():
        widget.destroy()

    # Foto toevoegen (resizen, PIL) -> Image resizen
    original_image = Image.open("ybear.png")
    resized_image = original_image.resize((300, 224))
    voorbeeld_image = ImageTk.PhotoImage(resized_image)

    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image

    # Font toevoegen tekst
    label_font = Font(family="Aniron", size=36, weight="bold")

    label = Label(venster, text="Dit is scherm A", font=label_font)
    button = Button(venster, text="Ga naar scherm B", command=lambda: maak_scherm_b_aan(venster))

    # Een image klikbaar maken
    label_image.bind("<Button-1>", lambda click_event: maak_scherm_b_aan(venster))

    label_image.pack()
    label.pack()
    button.pack()
