from tkinter import *

# km = mi / 0.62137


# get miles entry, convert to float, change to km, update km result label
def convert():
    miles = float(mile_entry.get())
    km = f"{round(miles / 0.62137, 1)}"
    kilometers_result.config(text=km)


# Main window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# Miles Entry
mile_entry = Entry(width=15)
mile_entry.insert(END, string="Enter Miles")
mile_entry.grid(row=0, column=1)

# Miles Unit
mile_unit = Label(text="Miles")
mile_unit.grid(row=0, column=2)

# Equal to text label
equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

# Km result label
kilometers_result = Label()
kilometers_result.grid(row=1, column=1)

# Km units
kilometer_unit = Label(text="Km")
kilometer_unit.grid(row=1, column=2)

# Calculate button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(row=2, column=1)


window.mainloop()
