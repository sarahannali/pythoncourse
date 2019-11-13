import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def left(self):
        return f"Deck of {len(self.cards)} cards"
    def build(self):
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range (1,14):
                letterCards = {1: "A", 11: "J", 12: "Q", 13: "K"}
                if value in letterCards:
                    self.cards.append(Card(suit, letterCards[value]))
                else:
                    self.cards.append(Card(suit,value))
    def count(self):
        return len(self.cards)
    def _deal(self, amount):
        if len(self.cards) == 0:
            raise ValueError ("All cards have been dealt")
        elif amount <= len(self.cards):
            dealtcards = self.cards[:amount:]
            del self.cards[:amount:]
        elif amount > len(self.cards):
            dealtcards = self.cards[:len(self.cards):]
            self.cards.clear()
        return dealtcards
    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            return self.cards
        else:
            raise ValueError ("Only full decks can be shuffled")
    def deal_card(self, amount=1):
        return self._deal(amount)