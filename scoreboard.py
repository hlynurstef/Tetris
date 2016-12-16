from game_settings import Settings
from text import Text

class Scoreboard():
    """A class to show the current score, level and lines."""

    def __init__(self, screen, game_stats):
        """Initialize the scoreboard."""
        self.screen = screen
        self.game_stats = game_stats
        self.settings = Settings()
        self.prep_score()
        self.prep_level()
        self.prep_lines()


    def prep_score(self):
        """Create a rendered image for score."""
        score = str(self.game_stats.score)
        self.score_image = Text(self.screen, score, 765, 120)


    def prep_level(self):
        """Create a rendered image for level."""
        level = str(self.game_stats.level)
        self.level_image = Text(self.screen, level, 725, 280)


    def prep_lines(self):
        """Create a rendered image for lines."""
        lines = str(self.game_stats.lines)
        self.lines_image = Text(self.screen, lines, 725, 400)


    def prep_scoreboard(self):
        """Preps every text on scoreboard."""
        self.prep_score()
        self.prep_level()
        self.prep_lines()


    def blitme(self, new_scoreboard):
        """Draw the scoreboard to the screen."""
        if new_scoreboard:
            self.prep_scoreboard()

        self.score_image.blitme()
        self.level_image.blitme()
        self.lines_image.blitme()
