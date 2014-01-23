"""
This module holds classes for creating an object oriented deck
of cards and the necessary methods for manipulating them
"""

import random


class PlayingCard:
    """
    Contains the attributes of a single playing card
    and methods for manipulating it in a game
    """
    def __init__(self):
        self.suit = None
        self.name = None
        self.value = None
        self.faceup = False

    def __str__(self):
        return ' '.join([self.name, 'of', self.suit])

    def flip(self):
        if self.faceup:
            self.faceup=False
        else:
            self.faceup=True


class CardDeck:
    """
    Contains 52 or more playing cards and methods for using them
    """
    def __init__(self, decks=1):
        self.deck = list()
        self.deck_count = decks

        self.suits = [
            'Clubs',
            'Diamonds',
            'Hearts',
            'Spades',
        ]

        self.names = [
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
        ]

        self.shuffle()

    def __len__(self):
        """
        Return number of card objects in the deck object list
        """
        return len(self.deck)

    def shuffle(self):
        """
        Initialize the deck with 52 or more cards
        """
        if self.deck:
            self.deck = list()

        max_decks = self.deck_count + 1  # +1 for range function

        for deck in range(1, max_decks):
            for suit in self.suits:
                for value, name in enumerate(self.names, start=1):
                    card = PlayingCard()
                    card.suit = suit
                    card.name = name
                    card.value = value
                    
                    self.deck.append(card)

    def draw(self):
        """
        Remove a random card from the deck and return it
        """
        try:
            card = random.choice(self.deck)
            self.deck.remove(card)
        except IndexError as err:
            card = None

        return card


class Blackjack:
    """
    Game logic for the card game Blackjack
    """
    def __init__(self, bet, decks=2, shuffle=25):
        self.deck_count = decks  # Number of card decks in the game deck
        self.shuffle = shuffle   # Percent of deck left for shuffle threshold
        self.player_bet = bet
        
        self.deck = CardDeck(decks=self.deck_count)
        self.card_total = len(self.deck)
        
        self.dealer = list()  # Initialize an empty hand for dealer
        self.player = list()  # Initialize an empty hand for player

        self.deal()

    def _shuffle_time(self):
        """
        Check if it is time to shuffle the deck by calculating
        the percentage of the cards remaining in the deck
        """
        remaining = len(self.deck)  # Current count of cards in the deck

        percentage_left = int( (remaining / self.card_total) * 100 )

        if ( percentage_left > 25 ):
            return False  # It isn't time to shuffle
        else:
            return True   # Or maybe it is
        
    def deal(self):
        """
        Deal out a new hand of cards to the dealer and player
        """
        if self.dealer:  # Has cards
            self.dealer = list()

        if self.player:  # Has cards
            self.player = list()

        dealer_first = self.deck.draw()
        dealer_second = self.deck.draw()

        dealer_second.flip()

        self.dealer.append(dealer_first)
        self.dealer.append(dealer_second)

        player_first = self.deck.draw()
        player_second = self.deck.draw()

        player_first.flip()
        player_second.flip()

        self.player.append(player_first)
        self.player.append(player_second)

    def check_hand(self, hand):
        """
        Check point value of the hand of cards and act appropriately
        """
        pass
    
    def hit(self, player_hand):
        """
        Retrieve a card from the deck, flip it face up, and add it to a hand
        """
        hit_card = self.deck.draw()
        hit_card.flip()
        player_hand.append(hit_card)

    def stay(self):
        """
        End the player's turn and pass control to the dealer
        """
        pass

