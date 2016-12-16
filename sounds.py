from pygame.mixer import Sound

class Sounds():
    """A class to store all sounds in Tetris."""

    def __init__(self):
        """Initialize Sounds."""
        self.title_music = Sound('sounds/music/title_music.ogg')
        self.a_type_music = Sound('sounds/music/a_type_music.ogg')
        self.b_type_music = Sound('sounds/music/b_type_music.ogg')
        self.c_type_music = Sound('sounds/music/c_type_music.ogg')
        self.high_score_music = Sound('sounds/music/high_score_music.ogg')
        self.level_up = Sound('sounds/sound_effects/LEVELUP.ogg')
        self.set_volume()


    def set_volume(self):
        """Set volume of music."""
        self.title_music.set_volume(.75)
        self.a_type_music.set_volume(.75)
        self.b_type_music.set_volume(.75)
        self.c_type_music.set_volume(.75)
        self.high_score_music.set_volume(.75)
        self.level_up.set_volume(.75)
