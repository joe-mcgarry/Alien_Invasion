import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from a ship"""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Builds bullet rect from scratch in top left with width and height
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # Matches bullet's midtop attribute to ship's - looks like firing from ship
        self.rect.midtop = game.ship.rect.midtop

        # Store bullet's position as decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Moves bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
