from os import system
import art


exit_bid = False


def enter_details(name,bid):
    bid_details[name] = bid


while exit_bid == False:
    cont_bid = True
    bid_details = {}
    while cont_bid == True:
        system("clear")
        print (art.logo)
        name = input ("what is your name?\n")
        bid = int(input ("what is the bid amount?\n"))
        enter_details(name,bid)

        forward = input ("Is there anyone else to bid? (Yes/No)\n").lower()

        while forward != "yes" and forward != "no":
            forward = input ("Please enter a correct value? (Yes/No)\n").lower()

        if forward == "no":
            cont_bid = False

    maximum = 0
    winner = ""

    for bidder in bid_details:
        bid_amt = bid_details[bidder]
        if bid_amt > maximum :
            maximum = bid_amt
            winner = bidder

    print (f"winner is {winner}\nBid amount is {maximum}")

    ex = input("exit?")

    if ex == "yes":
        exit_bid = True

    system("clear")

