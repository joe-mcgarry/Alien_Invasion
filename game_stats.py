class GameStats:
    """Tracks statistics for game"""

    def __init__(self, game):
        """initialise statistics"""
        self.settings = game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialise stats that change during the game"""
        self.ships_left = self.settings.ship_limit