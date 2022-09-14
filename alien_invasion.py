import sys
import pygame

class AlienInvasion:
    """Class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise and create resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main game loop"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Make most recently drawn screen visibile
            pygame.display.flip()
        
if __name__ == '__main__':
    #Make instance of game and run it
    ai = AlienInvasion()
    ai.run_game()