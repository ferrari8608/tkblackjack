class BlackjackPlayer:
    def __init__(self, playerid):
        self.name = playerid

        self.money = 500  # Start game with $500
        self.current_bet = 0
        
        self.highest_win = 0
        self.highest_loss = 0

        self.hand = list()

    def __iter__(self):
        return iter(self.hand)

    def __str__(self):
        return self.name


class BlackjackDealer:
    def __init__(self):
        self.name = "Dealer"

        self.hand = list()

    def __iter__(self):
        return iter(self.hand)

    def __str__(self):
        return self.name

