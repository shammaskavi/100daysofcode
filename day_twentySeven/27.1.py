from tkinter import *


# Initialize new object
window = Tk()

window.title("Python TKinter Day 2")
window.minsize(width = 1300, height = 900)

# Label
my_label = Label(text="Button not clicked", font=("Arial", 24, "bold"))
my_label.pack()
# Side can be right, left, bottom top, and the default value is top 

#Button
def button_clicked():
    # my_label['text'] = "Button got clicked"
    # new_label.config(text=f"Change from function {input_data}")
    new_text = input.get()
    new_label['text'] = new_text
    new_label.pack()


button = Button(text="Click", command=button_clicked)
button.pack()

# Entry
new_label = Label(text="Before Text entry")    
new_label.pack()
input = Entry(width=150)
input.pack()
new_label.config(text="Before Text Entry")
new_label.pack()



window.mainloop()