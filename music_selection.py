import pygame
from text import Text
class MusicSelection():
    """A class to handle selection of game type and music selection."""

    def __init__(self, screen, settings, sounds, music_channel):
        """Initialize GameMusicSelection."""
        self.screen = screen
        self.settings = settings
        self.sounds = sounds
        self.music_channel = music_channel
        self.music_pos = (0,0)
        self.text_blink_frequency = 350
        self.text_on = False
        self.music_selection = {(0,0): [self.sounds.a_type_music, 'A-TYPE'],
                                (1,0): [self.sounds.b_type_music, 'B-TYPE'],
                                (0,1): [self.sounds.c_type_music, 'C-TYPE'],
                                (1,1): [None, 'OFF']}
        self.time_of_last_draw = pygame.time.get_ticks()

    def prep_music_selection_text(self):
        """Create a rendered image for selection."""
        if self.music_selection[self.music_pos][0]:
            x_offset = 365
        else:
            x_offset = 285

        self.image = Text(self.screen, self.settings, self.music_selection[self.music_pos][1], self.settings.black,
                          self.music_pos[0]*320+x_offset, self.music_pos[1]*80+480)


    def right(self):
        """Move selection right if possible and play selected music."""
        if self.music_pos[0] == 0:
            self.music_pos = (1, self.music_pos[1])
            self.play_music()


    def left(self):
        """Move selection left if possible and play selected music."""
        if self.music_pos[0] == 1:
            self.music_pos = (0, self.music_pos[1])
            self.play_music()


    def up(self):
        """Move selection up if possible and play selected music."""
        if self.music_pos[1] == 1:
            self.music_pos = (self.music_pos[0], 0)
            self.play_music()


    def down(self):
        """Move selection down if possible and play selected music."""
        if self.music_pos[1] == 0:
            self.music_pos = (self.music_pos[0], 1)
            self.play_music()


    def play_music(self):
        """Play selected music."""
        self.music_channel.stop()
        if self.music_selection[self.music_pos][0]:
            self.music_channel.play(self.music_selection[self.music_pos][0], -1)


    def blitme(self):
        """Draw the current selection to the screen."""
        current_time = pygame.time.get_ticks()
        if current_time - self.time_of_last_draw > self.text_blink_frequency:
            self.text_on = not self.text_on
            self.time_of_last_draw = current_time
        if self.text_on:
            self.prep_music_selection_text()
            self.image.blitme()
