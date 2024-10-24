import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Circle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function.
    populate_main_window(frm_main)

    # Start the tkinter loop.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program."""

    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius (1 - 100):")

    # Create an integer entry box where the user will enter the radius.
    ent_radius = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=100)

    # Create a label that will display the results.
    lbl_area = Label(frm_main, width=15)
    lbl_area_units = Label(frm_main, text="square units")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(    row=0, column=0, padx=3, pady=3)
    ent_radius.grid(    row=0, column=1, padx=3, pady=3)
    lbl_area.grid(      row=1, column=0, padx=3, pady=3)
    lbl_area_units.grid(row=1, column=1, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=2, sticky="w")

    def calculate(event):
        """Compute and display the area of the circle."""
        try:
            # Get the radius from the user.
            radius = ent_radius.get()

            # Compute the area of the circle.
            area = math.pi * (radius ** 2)

            # Display the area.
            lbl_area.config(text=f"{area:.2f}")

        except ValueError:
            # When the user deletes all digits, clear the area label.
            lbl_area.config(text="")

    def clear():
        """Clear all the inputs and outputs."""
        ent_radius.clear()
        lbl_area.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the radius entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the radius entry box.
    ent_radius.focus()


if __name__ == "__main__":
    main()
