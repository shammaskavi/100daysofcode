from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}
toLearn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    toLearn =original_data.to_dict(orient="records")
else:
    toLearn =  data.to_dict(orient="records")


def next_card():
    global currentCard, flip_timer
    window.after_cancel(flip_timer)
    currentCard = random.choice(toLearn)
    canva.itemconfig(cardTitle, text = "French",fill = 'black')
    canva.itemconfig(cardWord, text = currentCard['French'], fill = 'black')
    canva.itemconfig(cardBackground, image = cardFrontImg)
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canva.itemconfig(cardTitle, text = "English", fill = "white")
    canva.itemconfig(cardWord, text = currentCard['English'], fill = "white")
    canva.itemconfig(cardBackground, image = cardBackImg)

def is_known():
    toLearn.remove(currentCard)
    print(len(toLearn))
    next_card()
    data = pandas.DataFrame(toLearn)
    data.to_csv("data/words_to_learn.csv", index = False)
    


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx= 50, pady= 50)

flip_timer = window.after(3000, func = flip_card)

canva = Canvas(width= 800, height=526)
cardFrontImg = PhotoImage(file = "images/card_front.png")
cardBackImg = PhotoImage(file = "images/card_back.png")
cardBackground = canva.create_image(400, 263, image=cardFrontImg)
canva.config(background=BACKGROUND_COLOR, highlightthickness=0)
cardTitle = canva.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
cardWord = canva.create_text(400, 263, text = "word", font = ("Ariel", 60, "bold"))
canva.grid(row=0, column=0, columnspan=2)

#unknownButton
crossImage = PhotoImage(file = "images/wrong.png")
unknownButton = Button(image=crossImage, bg=BACKGROUND_COLOR, borderwidth=0,command=next_card)
unknownButton.grid(row= 1, column=0)

#knowButton
rightImage = PhotoImage(file = "images/right.png")
unknownButton = Button(image=rightImage, bg=BACKGROUND_COLOR,borderwidth=0,command=is_known)
unknownButton.grid(row= 1, column=1)

next_card()
window.mainloop()