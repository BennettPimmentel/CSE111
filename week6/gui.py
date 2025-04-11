import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
import math

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Creative Circle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program."""
    
    lbl_radius = Label(frm_main, text="Radius (in cm):", font=("Arial", 12, "bold"))
    ent_radius = FloatEntry(frm_main, width=20, lower_bound=0, upper_bound=100, default=None)
    lbl_radius_units = Label(frm_main, text="cm", font=("Arial", 10))

    lbl_area = Label(frm_main, text="Area: ", font=("Arial", 12, "bold"))
    lbl_result = Label(frm_main, width=10, text="", font=("Arial", 14))

    btn_clear = Button(frm_main, text="Clear", font=("Arial", 12), bg="#FF6347", fg="white")
    
    status_bar = Label(frm_main, text="Enter a radius to calculate the area", anchor="w", relief="sunken", height=2, font=("Arial", 10))
    status_bar.grid(row=3, column=0, columnspan=3, sticky="we", padx=3, pady=3)

    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_area.grid(row=1, column=0, padx=3, pady=3)
    lbl_result.grid(row=1, column=1, padx=3, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=3, sticky="w")
    
    def calculate(event):
        """Calculate the area of the circle."""
        try:
            radius = ent_radius.get()
            if radius <= 0:
                raise ValueError("Radius must be positive.")

            area = math.pi * (radius ** 2)
            lbl_result.config(text=f"{area:.2f} cm²")
            status_bar.config(text="Area calculated successfully!", fg="green")

        except ValueError as e:
            lbl_result.config(text="")
            status_bar.config(text=str(e), fg="red")

    def clear():
        """Clear all inputs and outputs."""
        ent_radius.clear()
        lbl_result.config(text="")
        status_bar.config(text="Enter a radius to calculate the area", fg="black")
        ent_radius.focus()

    ent_radius.bind("<KeyRelease>", calculate)
    btn_clear.config(command=clear)

    ent_radius.focus()

if __name__ == "__main__":
    main()
