import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        return "{} of {}".format(self.value, self.suit)
        
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def points(self):
        return {'2':1 ,'3':2 ,'4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}

class Shuffle(Deck):
    def shuffle(self):
        random.shuffle(self.cards)

    def pick(self):
        return self.cards.pop()

deck_1 = Shuffle()
deck_1.shuffle()
sum_1 = 0
print("Player 1 picks:")
for i in range(5):
    card = deck_1.pick()
    player_1 = card.show()
    print(player_1, end = "----->")
    point = deck_1.points()[player_1.split(' ')[0]]
    print(point)
    sum_1 += point
print("Total points of Player 1:", sum_1)

deck_2 = Shuffle()
deck_2.shuffle()
sum_2 = 0
print("\nPlayer 2 picks:")
for i in range(5):
    card = deck_2.pick()
    player_2 = card.show()
    print(player_2, end = "----->")
    point = deck_2.points()[player_2.split(' ')[0]]
    print(point)
    sum_2 += point
print("Total points of Player 2:", sum_2)

if sum_1 > sum_2:
    print("\nPlayer 1 Wins")
elif sum_1 < sum_2:
    print("\nPlayer 2 Wins")
else:
    print("\nTIE")