"""This module holds classes for creating an object oriented deck
of cards and the necessary methods for manipulating them
"""
__all__ = ['PlayingCard', 'CardDeck']

import random
from collections import deque


class PlayingCard(object):
    """Contains the attributes of a single playing card and methods for
    manipulating it in a game
    """

    def __init__(self):
        self.suit = None     # Card suit, e.g. Spades
        self.name = None     # Name string, e.g. King
        self.id = None       # Number identifier, [1-13]
        self.faceup = False  # Face up or down, boolean value
        self.value = None    # Point value within a game

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return other + self.value

    def __sub__(self, other):
        return self.value - other

    def __rsub__(self, other):
        return other - self.value

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __int__(self):
        return int(self.value)
    
    def __str__(self):
        return '{0} of {1}'.format(self.name, self.suit)

    def flip(self):
        """Set faceup value to False if True and vice versa."""
        
        if self.faceup:
            self.faceup = False
        else:
            self.faceup = True

    def set_attributes(self, name, suit, id_no=0):
        """Set the card's name, suit, and identification number."""
        
        self.name = str(name)
        self.suit = str(suit)
        self.id = int(id_no)

    def assign_value(self, points):
        """Set the card's point value."""
        
        self.value = int(points)


class CardDeck(object):
    """Contains 52 or more playing cards and the methods for using them."""

    def __init__(self, decks=1):
        self.deck = deque()
        self.deck_count = int(decks)
        self.shuffle_count = self.deck_count * 7

        self.suits = (
            'Clubs',
            'Diamonds',
            'Hearts',
            'Spades',
        )

        self.names = (
            'Ace',
            'Two',
            'Three',
            'Four',
            'Five',
            'Six',
            'Seven',
            'Eight',
            'Nine',
            'Ten',
            'Jack',
            'Queen',
            'King',
        )

        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

    def __getitem__(self, index):
        return self.deck[index]
        
    def shuffle(self):
        """Initialize the deck with 52 or more cards."""

        if self.deck:
            self.deck = deque()

        max_decks = self.deck_count + 1  # +1 for range function

        for deck in range(1, max_decks):
            for suit in self.suits:
                for num, name in enumerate(self.names, start=1):
                    card = PlayingCard()
                    card.set_attributes(name, suit, num)
                    self.deck.append(card)

        for number in range(self.shuffle_count):
            random.shuffle(self.deck)
        
    def draw(self):
        """Remove the first card from the deck and return it."""

        return self.deck.popleft()
