from tkinter import Tk

from Schoolopdrachten.Oefenen.Workshop.scherm_a import maak_scherm_a_aan


def main():
    root = Tk()
    root.geometry("500x500")
    root.title("Workshop app")
    maak_scherm_a_aan(root)

    root.mainloop()


if __name__ == '__main__':
    main()
