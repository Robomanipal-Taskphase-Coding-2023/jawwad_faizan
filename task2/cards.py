import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def is_pair(self, card1, card2):
        rank_order = "2345678910JQKA"
        rank1, rank2 = card1.rank, card2.rank
        suit1, suit2 = card1.suit, card2.suit

        if (rank1 in rank_order and rank2 in rank_order) or (rank1 == "A" and rank2 == "K") or (rank1 == "K" and rank2 == "A"):
            if abs(rank_order.index(rank1) - rank_order.index(rank2)) == 1 and suit1 == suit2:
                return True

        return False

# Example usage:
deck = Deck()
deck.shuffle()

card1 = deck.cards[0]
card2 = deck.cards[1]

print("Shuffled Deck:")
for card in deck.cards:
    print(card)

if deck.is_pair(card1, card2):
    print(f"{card1} and {card2} form a pair.")
else:
    print(f"{card1} and {card2} do not form a pair.")
