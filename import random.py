# Name: Zachary Schider
# Date: 10/16/2024
# Period: 3

import random
def roll_random(low, high):
    # Needed for random rolling for all programs
    return random.randrange(low, high)

def card_suit():
    # Function determines the suit of the card (Hearts, Clubs, Diamonds, Spades)
    num = roll_random(1, 102)
    if num >= 1 and num <= 25:
        return "Hearts"
    elif num >= 26 and num <= 50:
        return "Clubs"
    elif num >= 51 and num <= 75:
        return "Diamonds"
    elif num >= 76 and num <= 100:
        return "Spades"
    # The Joker Card has a 2% chance of being picked (2/100)
    elif num >= 101:
        return "Joker"

def card_face():
    # Function determines the face of the card (the numbers)
    num = roll_random(1, 10)
    if num == 1:
        return "Ace"
    elif num >= 2 and num <= 9:
        num_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return num_list[num-2]
    # If num rolled equals 10, it runs royal function for the cards above 10
    elif num == 10:
        return royal()

def royal():
    # Function determines the royalty of the card determined by the num from card_face()
    num = roll_random(1, 4)
    if num == 1:
        return "Ten"
    elif num == 2:
        return "Jack"
    elif num == 3:
        return "Queen"
    elif num == 4:
        return "King"
    
def draw_card(multiplicity):
    # i serves as a looping method for the draws
    i = 0
    while i < multiplicity:
        # Once i = multiplicity, the loop is stopped (so i must be increasing by 1 each loop)
        i = i + 1
        faceName = card_face()
        suitName = card_suit()
        # Checks if the card is Joker or not before printing
        if suitName == "Joker":
            print("You have drawn the Joker.")
        else:
            print("You have drawn the", faceName, "of", suitName + ".")

# draws = How many cards you want to draw at once
draws = 2
draw_card(draws)

# Enhancements: Multiple Draws, Joker Card