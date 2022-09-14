import imp
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main game loop"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make instance of game and run it
    ai = AlienInvasion()
    ai.run_game()
