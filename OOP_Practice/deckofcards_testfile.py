import unittest
from deckofcards_practice import Card, Deck

class CardClass(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def testInit(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")
    
    def testRepr(self):
        """repr should return "VALUE of SUIT"""
        self.assertEqual(repr(self.card),"A of Hearts")

class DeckClass(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def testInit(self):
        """when deck is built, cards should become because none have been dealt"""
        self.assertIsInstance(self.deck.cards, list)
        self.assertEqual(len(self.deck.cards),52)

    def testLeft(self):
        """should return "Deck of (# of cards) cards", even after some are dealt"""
        self.assertEqual(self.deck.left(),"Deck of 52 cards")
        self.deck.deal_card(5)
        self.assertEqual(self.deck.left(), "Deck of 47 cards")

    def testOverRequest(self):
        """overrequesting should return all cards left and empty the deck"""
        overrequest = self.deck.deal_card(100)
        self.assertEqual(len(overrequest), 52)
        self.assertEqual(self.deck.cards,[])

    def testDealEmptyDeck(self):
        """dealing from an empty deck should raise a ValueError"""
        self.deck.deal_card(52)
        with self.assertRaises(ValueError):
            self.deck.deal_card()

    def testShuffleOnlyFull(self):
        """shuffle should only shuffle a full deck"""
        self.deck.deal_card(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()