from art import logo
import random

print(logo)

print("Welcome to the number guessing game.")

print("I'm thinking of a number between 1 and 50")

secretNumber = random.randint(1, 50)

print(f"Psst! The secret number is, {secretNumber}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

if difficulty == 'easy':
    chances = 10
    print(f"You have {chances} attempts left to guess the number")
elif difficulty == 'hard':
    chances = 5
    print(f"You have {chances} attempts left to guess the number")


for i in range(chances):
    guess = int(input("Make a guess: "))
    if guess == secretNumber:
        print("Correct guess")
        print("You win")
        break
    else:
        if guess > secretNumber:
            print("Too High")
        else:
            print("Too Low")
        chances -= 1
        print(f"You have {chances} attempts left to guess the number")
