import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Jack", 2)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame()

    def test_check_for_ace__True(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_check_for_ace__False(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card2))

    def test_highest_card__card2(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))

    def test_highest_card__card1(self):
        self.card1 = Card("Queen", 5)
        self.assertEqual(self.card1, self.cardgame.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 3", self.cardgame.cards_total(self.cards))
    