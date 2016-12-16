from pygame.font import Font
from game_settings import Settings

class Text():
    """A class representing text."""

    def __init__(self, screen, text, x, y):
        """Initialize text."""
        self.screen = screen
        self.settings = Settings()
        self.font = Font(self.settings.font, self.settings.font_size)
        self.image = self.font.render(text, True, self.settings.black)
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y


    def blitme(self):
        """Draw the text at it's current position."""
        self.screen.blit(self.image, self.rect)
