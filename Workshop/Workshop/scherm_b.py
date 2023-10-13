from tkinter import Label, Button


def maak_scherm_b_aan(venster):
    from scherm_a import maak_scherm_a_aan

    for widget in venster.winfo_children():
        widget.destroy()

    label = Label(venster, text="Dit is scherm B")
    button = Button(venster, text="Ga naar scherm A", command=lambda: maak_scherm_a_aan(venster))

    label.pack()
    button.pack()
