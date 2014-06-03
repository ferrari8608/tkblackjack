__all__ = ['BlackjackDealer', 'BlackjackPlayer']

class BlackjackDealer(object):
    """Contains attributes and operators for a Blackjack card dealer."""

    def __init__(self):
        self.name = "Dealer"
        self.hand = list()

    def __iter__(self):
        return iter(self.hand)

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.hand


class BlackjackPlayer(BlackjackDealer):
    """Inherits everything from BlackjackDealer and adds attributes and
    operators for manipulating money and keeping score.
    """

    def __init__(self, playerid):
        self.name = playerid
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
