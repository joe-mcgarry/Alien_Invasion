import pygame

class Alien(Sprite):
    """A class to represent one alien in the alien fleet"""

    def __init__(self, game):
        """Initialise the alien and set its starting point"""
        super().__init__()
        self.screen = game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start aliens in top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position
        self.x = float(self.rect.x)