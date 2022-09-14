import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, game) -> None:
        """Initialise the ship and set the starting position"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect() #Access screen's rect properties

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Updates ship's position based on movement flag"""
        # Don't use elif because right key will take priority
        # Updating ship's x value, not rect's 
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        # Updates rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)