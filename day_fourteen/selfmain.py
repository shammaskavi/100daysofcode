from art import logo, vs
from game_data import data
import random
import os


def format_data(account):
    """Format the account data into printable format."""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_guess(user_guess, follower_a, follower_b):
    """Check if the guess is correct or not using a if statement"""
    if user_guess == 'a' and follower_a > follower_b:
        return True
    elif user_guess == 'b' and follower_b > follower_a:
        return True
    else:
        return False


# display art

print(logo)
score = 0
can_continue = True
while can_continue:
    # Generate  a random account from the game data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        random.choice(data)

    # Format the acc data into printable format
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user for a guess
    user_guess = input("Who has more followers: 'A' or 'B': ").lower()

    # Check if user is correct
    # Get follower count of each account
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']

    # Use if statement
    # Function mentioned at the top
    # the check_guess() function
    is_correct = check_guess(user_guess, follower_a, follower_b)

    # Give user a feedback on their guess

    if is_correct == True:
        print("You're right")
        score += 20
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("You Loose")
        can_continue = False
        if score >= 100:
            print(f"Ohh la la, {score}look at you gooooo!!!")
        elif score >= 80:
            print(f"{score} huh, There's potential")
        elif score >= 60:
            print(f"{score}is veerry average, You'll die an average death")
        elif score >= 40:
            print(f"Oh my {score} is bad")
        else:
            print(f"You're score is not worth showing")

    # score keeping

    # Make gamer repeatable

    # Making account at pos B becomethe next acc at pos and
    # Clear the screen between rounds
