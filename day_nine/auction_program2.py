from art import logo
print(logo)


def clear():
    print("\n" * 50)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    print(f"the winner is {winner} ${highest_bid}")


bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    # this is how to add to dictionary
    bids[name] = price
    should_continue = input("Are  there any other bidders? Type 'yes' or 'no'")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()
