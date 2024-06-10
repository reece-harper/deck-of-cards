from ast import In
from random import shuffle
suits = ["♥", "♦", "♣", "♠"]
deck = []



for item in suits:
    for x in range(1, 14):
        if x == 11:
            deck.append("J" + item)
        elif x == 12:
            deck.append("Q" + item)
        elif x == 13:
            deck.append("K" + item)
        elif x == 14:
            deck.append("A" + item)
        else:
            deck.append(f"{x}" + item)

print(deck)
input("please press enter to shuffle")
shuffle(deck)
print(deck)
      