from tkinter import *


def miles_to_km():
    conv_miles = float(miles_input.get())
    conv_km = round(conv_miles * 1.609)
    answer_in_km.config(text=f"{conv_km}")


window = Tk()
window.title("My First GUI Program")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
miles_label = Label(text="miles", font=("Ariel", 24, "bold"))
miles_label.grid(column=2, row=0)

# Label
is_equal_to_label = Label(text="is equal to", font=("Ariel", 24, "bold"))
is_equal_to_label.grid(column=0, row=1)

# Label
km_label = Label(text="Km", font=("Ariel", 24, "bold"))
km_label.grid(column=2, row=1)

# Label
answer_in_km = Label(text="0", font=("Ariel", 24, "bold"))
answer_in_km.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Entry
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

window.mainloop()
