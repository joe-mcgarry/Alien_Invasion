import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, game) -> None:
        """Initialise the ship and set the starting position"""
        self.screen = game.screen 
        self.screen_rect = game.screen.get_rect() #Access screen's rect properties

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)