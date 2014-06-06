"""This module holds classes for creating an object oriented deck
of cards and the necessary methods for manipulating them
"""
__all__ = ['PlayingCard', 'CardDeck']

import random
from collections import deque
from players import *

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

    def face(self):
        """Return True or False whether or not the card is face up."""

        return self.faceup

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

        for deck_shuffle in range(self.shuffle_count):
            random.shuffle(self.deck)
        
    def draw(self):
        """Remove the first card from the deck and return it."""

        return self.deck.popleft()


class Blackjack:
    """Game logic for the card game Blackjack"""

    def __init__(self, bet, decks=2, shuffle=25, debug=False):
        self.deck_count = decks  # Number of card decks in the game deck
        self.shuffle = shuffle   # Percent of deck left for shuffle threshold
        self.player_bet = bet
        self.verbose = debug

        self.deck = CardDeck(decks=self.deck_count)
        self._assign_values()
        self.card_total = len(self.deck)
        
        self.player = BlackjackPlayer()
        self.dealer = BlackjackDealer()

    def _assign_values(self):
        for card in self.deck:
            if card.id > 9:
                card.assign_value(10)
            else:
                card.assign_value(card.id)

    def _shuffle_time(self):
        """Check if it is time to shuffle the deck by calculating the
        percentage of the cards remaining in the deck
        """

        remaining = len(self.deck)  # Current count of cards in the deck
        percentage_left = int((remaining / self.card_total) * 100)

        if ( percentage_left > 25 ):
            return False  # It isn't time to shuffle
        else:
            return True   # Or maybe it is
        
    def deal(self):
        """Deal out a new hand of cards to the dealer and player."""

        if self.dealer:  # Has cards in hand
            self.dealer.reset()

        if self.player:  # Has cards in hand
            self.player.reset()

        dealer_first = self.deck.draw()
        dealer_second = self.deck.draw()
        dealer_second.flip()
        self.dealer.take_card(dealer_first)
        self.dealer.take_card(dealer_second)

        player_first = self.deck.draw()
        player_second = self.deck.draw()
        player_first.flip()
        player_second.flip()
        self.player.take_card(player_first)
        self.player.take_card(player_second)

        if self.verbose:
            print('Player bets:', self.player_bet)
            for player in (self.player, self.dealer):
                print(player, 'dealt:')
                for card in player:
                    if card.face():
                        print(' '*3, str(card)+':', 'face up')
                    else:
                        print(' '*3, str(card)+':', 'face down')
            
    def check_hand(self, player):
        """Check point value of the hand of cards and act appropriately."""

        total = player.score()
        if total > 21:
            status = 'bust'
        elif total == 21:
            status = 'win'
        else:
            status = 'okay'

        if self.verbose:
            print(total, 'points')
            
        return status
    
    def hit(self, player):
        """Retrieve a face up card from the deck, and add it to a hand."""

        hit_card = self.deck.draw()
        hit_card.flip()
        player.take_card(hit_card)

        if self.verbose:
            print(player, 'receives', hit_card)

    def stay(self):
        """End the player's turn and pass control to the dealer."""

        pass
