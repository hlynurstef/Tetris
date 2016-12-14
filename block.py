import pygame
from pygame.sprite import Sprite
from game_settings import Settings

class Block(Sprite):
    """A class representing a single block."""

    def __init__(self, screen, color, x, y):
        """Initialize the Block."""
        super(Block, self).__init__()
        self.screen = screen
        self.settings = Settings()

        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        """Draw the block at its current location."""
        self.screen.blit(self.image, self.rect)
