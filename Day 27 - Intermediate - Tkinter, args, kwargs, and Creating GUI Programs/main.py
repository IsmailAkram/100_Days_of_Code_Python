from tkinter import *

def calculate_button_clicked():
    # print("I got clicked")
    new_text = float(input.get()) * 1.609
    km_value.config(text=new_text)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=2, row=1)

# Labels
# my_label["text"] = "New Text"
miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=3, row=1)

is_equal_to_label = Label(text="is equal to", font=("Arial", 16))
is_equal_to_label.grid(column=1, row=2)

km_value = Label(text="0", font=("Arial", 16))
km_value.grid(column=2, row=2)

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=3, row=2)

# Button
calculate_button = Button(text="Calculate", command=calculate_button_clicked) # function call only when clicked, so we don't use ()
calculate_button.grid(column=2, row=3)

window.mainloop()