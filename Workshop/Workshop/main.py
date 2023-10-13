from tkinter import Tk, Label, Button, Entry, PhotoImage


def print_naar_console():
    print("De button is geklikt")


def verander_label_tekst(label, tekst):
    label["text"] = tekst
    pass


def main():

    root = Tk()
    root.geometry("400x400")
    root.title("Hello World!")
    hello_world_label = Label(root, text="Hello world")
    button = Button(root, text="Druk mij", command=lambda: verander_label_tekst(hello_world_label, gebruikers_input.get()))

    gebruikers_input = Entry(root, bd=1)
    logo_image = PhotoImage(file="../images/python_logo.png")
    logo_frame = Label(image=logo_image, text="Python Logo", compound="center", fg="black")

    logo_frame.pack()
    hello_world_label.pack()
    gebruikers_input.pack()
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
