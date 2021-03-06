from text import Text

class Scoreboard():
    """A class to show the current score, level and lines."""

    def __init__(self, screen, settings, game_stats):
        """Initialize the scoreboard."""
        self.screen = screen
        self.settings = settings
        self.game_stats = game_stats
        self.prep_score()
        self.prep_level()
        self.prep_lines()
        self.prep_scoreboard()


    def prep_score(self):
        """Create a rendered image for score."""
        score = str(self.game_stats.score)
        self.score_image = Text(self.screen, self.settings, score, self.settings.black, 765, 120)


    def prep_level(self):
        """Create a rendered image for level."""
        level = str(self.game_stats.level)
        self.level_image = Text(self.screen, self.settings, level, self.settings.black, 725, 280)


    def prep_lines(self):
        """Create a rendered image for lines."""
        lines = str(self.game_stats.lines)
        self.lines_image = Text(self.screen, self.settings, lines, self.settings.black, 725, 400)


    def prep_scoreboard(self):
        """Preps every text on scoreboard."""
        self.prep_score()
        self.prep_level()
        self.prep_lines()


    def blitme(self):
        """Draw the scoreboard to the screen."""
        self.prep_scoreboard()
        self.score_image.blitme()
        self.level_image.blitme()
        self.lines_image.blitme()
