from tkinter import *
import random
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

noOfLetters = 9
noOfSymbols = 2
noOfDigits = 2
password_list = []

def generate_entry():
    if password_input.get() == 0:
        pass
    else:
        for char in range(1, noOfLetters + 1):
            global password_list
            password_list.append(random.choice(letters))

        for char in range(1, noOfSymbols + 1):
            password_list += random.choice(symbols)

        for char in range(1, noOfDigits + 1):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        password_input.insert(0, password)
        return password
        print(password)
        print(password_list)
        password_list.clear()

        
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_entry():

    website = website_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Invalid Details", message="Enter the details correctly")
    else:
        is_okay = messagebox.askokcancel(title=website_input.get(), message=f"These are the detials entered:\nEmail: {info_input.get()}\nPassword: {password_input.get()}\nIs it okay to save ?")

        if is_okay:
            with open("password.txt", mode= "a") as file:
                file.write(f"{website} | {info_input.get()} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0, END)
        
# ---------------------------- SEARCH PASSWORD ------------------------------- #

    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canva = Canvas(width=200, height= 200,highlightthickness=0)


img = PhotoImage(file = "logo.png")
canva.create_image(100, 100, image = img,)
canva.grid(column=1, row=0)

#Lablels
website_label = Label(text="Website:")
website_label .grid(column=0, row=1 )

info_label = Label(text="Email/Username:")
info_label.grid(column=0, row=2 )

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#Buttons 
search_button = Button(text= "Search", command= search_entry, width=13)
search_button.grid(column= 2, row = 1)

generate_button = Button(text="Generate Password", highlightthickness=0, command= generate_entry)
generate_button.grid(column=2, row=3,)

add_button = Button(text="Add", command= add_entry, width=36)
add_button.grid(column=1, row=4, columnspan=2)


#Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()


info_input = Entry(width=35)
info_input.grid(column=1, row=2, columnspan=2)
info_input.insert(0, "shammaskavi@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3,)





window.mainloop()