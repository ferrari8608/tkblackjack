__all__ = ['BlackjackDealer', 'BlackjackPlayer']

class BlackjackDealer(object):
    """Contains attributes and operators for a Blackjack card dealer."""

    def __init__(self):
        self.name = 'Dealer'
        self.hand = list()
        self.score = 0

    def __iter__(self):
        return iter(self.hand)

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.hand

    def reset(self):
        """Empty the hand."""
        
        self.hand = list()

    def score(self):
        """Return point value total of cards in the player's hand."""

        return sum(self.hand)

    def take_card(self, card):
        """Add a card to the hand."""

        self.hand.append(card)


class BlackjackPlayer(BlackjackDealer):
    """Inherits everything from BlackjackDealer and adds attributes and
    operators for manipulating money and keeping score.
    """

    def __init__(self, name='Player'):
        self.name = name
        self.money = 500  # Start game with $500
        self.current_bet = 0
        self.highest_win = 0
        self.highest_loss = 0

    def __add__(self, addition):
        return self.money + addition

    def __iadd__(self, addition):
        self.money += addition

    def __sub__(self, subtraction):
        return self.money - subtraction

    def __isub__(self, subtraction):
        self.money -= subtraction

    def set_bet(self, bet):
        """Set the current bet value."""

        self.current_bet = int(bet)

    def winner(self, winnings):
        """Add money won to self.money then check and return highest win."""

        self.money += winnings
        if winnings > self.highest_win:
            self.highest_win = winnings

        return self.highest_win

    def loser(self, loss):
        """Subtract money from self.money then check and return highest loss."""

        self.money -= loss
        if loss > self.highest_loss:
            self.highest_loss = loss

        return self.highest_loss
    
    def check_money(self):
        """Return player's current wallet value."""
        
        return self.money
