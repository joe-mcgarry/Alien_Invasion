class GameStats:
    """Tracks statistics for game"""

    def __init__(self, game):
        """initialise statistics"""
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialise stats that change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
