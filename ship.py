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

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Updates ship's position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)