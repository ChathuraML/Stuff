import art
import random

cards = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A'] * 4
print(art.logo)
print('<<<<<----------------Good Luck!----------------->>>>\n')
Values = {'J':10 ,'Q':10,'K':10,'A':11}

def card_values(card):
    if isinstance(card, int):
        return card
    return Values[card]

def total(player_total, com_total):
    if player_total > 21:
            print("\nBust!, You went over.")
    else:
        if player_total > com_total:
            print("\nYou won! :D")
        elif player_total < com_total:
            print("\nYou lose! :(")
        else:
            print("\nIt's Tie, let's push")

    print("\n^~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~^")

   
another_card = True

while another_card:
    n1 = random.choice(cards)
    n2 = random.choice(cards)
    total1 = card_values(n1) + card_values(n2)

    if total1 > 21 and ("A" in [n1,n2]):
        total1 -= 10
    
    print(f"Your cards: [{n1}, {n2}], current score:  {total1}")

    com_n1 = random.choice(cards)
    com_n2 = random.choice(cards)
    com_total = card_values(com_n1) + card_values(com_n2)

    print(f"Computer's first card: [{com_n1}]")

    answer = input("\nType 'y' to get another card, type 'n' to pass: ")
    print("\n")
    if answer == 'y':
        n3 = random.choice(cards)
        total1 = total1 + card_values(n3)
        print(f"Your final hand: [{n1}, {n2}, {n3}], final score:  {total1}")
        print(f"Computer's final hand: [{com_n1}, {com_n2}], final score:  {com_total}")
        total(total1, com_total)
        break
    else:
        print(f"Computer's final hand: [{com_n1}, {com_n2}], final score:  {com_total}")
        print(f"Your cards: [{n1}, {n2}], current score:  {total1}")
        total(total1, com_total)
        another_card = False

