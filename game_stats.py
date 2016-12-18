class GameStats():
    """A class to hold all game related stats."""

    def __init__(self, sounds):
        """Initialize game settings."""
        self.reset_game_stats()
        self.speed = [800, 717, 617, 550, 467, 383, 300, 217, 133, 100, 83, 83,
                      83, 67, 67, 67, 50, 50, 50, 33, 33, 33, 33, 33, 33, 33,
                      33, 33, 33, 33, 17]
        self.base_line_values = {1: 40, 2: 100, 3: 300, 4: 1200}
        self.sounds = sounds


    def reset_game_stats(self):
        """Reset all game stats."""
        self.score = 0
        self.level = 0
        self.lines = 0
        self.fall_frequency = 800


    def increment_lines(self, num_lines):
        """
        Increment lines by number and if lines are a multiple of 10
        then we increment the level and fall frequency as well.
        """
        for i in range(num_lines):
            self.lines += 1
            if not self.lines % 10:
                self.level += 1
                self.set_level_fall_frequency()
                self.sounds.level_up.play()

        self.score += self.base_line_values[num_lines] * (self.level + 1)


    def add_score(self, score):
        """Adds to total score."""
        self.score += score


    def key_down_fall_frequency(self):
        """Sets fall frequency to 100 when player presses down key."""
        self.fall_frequency = 50


    def set_level_fall_frequency(self):
        """Sets fall frequency according to the current level."""
        self.fall_frequency = self.speed[self.level]
