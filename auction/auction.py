import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\

'''

print(logo)
def find_highest_bidder(bidding_dic):
    max = 0
    winner = ""
    for key in bidding_dic:
        if bidding_dic[key] > max:
            max = bidding_dic[key]
            winner = key

    print(f"The winner is {winner} with a bid of ${max}.")
<<<<<<< HEAD
    
=======

>>>>>>> app_branch
auction = {}
next = True
while next:
    name = input("What is your name?: ")
    bid = int(input("\nWhat is your bid?: "))

    auction[name] = bid

    answer = input("Is there other users who want to bid(y/n)? ")
    if answer == "y":
        os.system('cls')
    else:
        next = False
        os.system('cls')
        find_highest_bidder(auction)

<<<<<<< HEAD

#print(auction)
=======
>>>>>>> app_branch
