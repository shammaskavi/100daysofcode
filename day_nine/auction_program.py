# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
completed = False


def clear():  # Prints 50 blank lines
    print("\n" * 50)


def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(
        f'The winner of the bidding is {winner} with the highest bid of {bidding_record[winner]}')


bidders = {}
while not completed:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? :$"))
    bidders[name] = bid
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        print("finding the highest price")
        completed = True
        highest_bid(bidders)

    elif should_continue == 'yes':
        clear()

# bidders = {}
# bidders[name] = bid

print(bidders)
