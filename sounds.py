from pygame.mixer import Sound

class Sounds():
    """A class to store all sounds in Tetris."""

    def __init__(self):
        """Initialize Sounds."""
        # Music
        self.title_music = Sound('sounds/music/title_music.ogg')
        self.a_type_music = Sound('sounds/music/a_type_music.ogg')
        self.b_type_music = Sound('sounds/music/b_type_music.ogg')
        self.c_type_music = Sound('sounds/music/c_type_music.ogg')
        self.high_score_music = Sound('sounds/music/high_score_music.ogg')

        # Sound Effects
        self.board_land_after_clear = Sound('sounds/sound_effects/board_land_after_clear.ogg')
        self.clear_line = Sound('sounds/sound_effects/clear_line.ogg')
        self.game_over = Sound('sounds/sound_effects/game_over.ogg')
        self.game_over_wall = Sound('sounds/sound_effects/game_over_wall.ogg')
        self.level_up = Sound('sounds/sound_effects/level_up.ogg')
        self.move_sideways = Sound('sounds/sound_effects/move_sideways.ogg')
        self.option_select = Sound('sounds/sound_effects/option_select.ogg')
        self.pause = Sound('sounds/sound_effects/pause.ogg')
        self.rotate = Sound('sounds/sound_effects/rotate.ogg')
        self.shape_land = Sound('sounds/sound_effects/shape_land.ogg')
        self.switch_option_screen = Sound('sounds/sound_effects/switch_option_screen.ogg')
        self.tetris_clear = Sound('sounds/sound_effects/tetris_clear.ogg')

        self.set_volume()


    def set_volume(self):
        """Set volume of Sounds."""
        self.title_music.set_volume(.75)
        self.a_type_music.set_volume(.75)
        self.b_type_music.set_volume(.75)
        self.c_type_music.set_volume(.75)
        self.high_score_music.set_volume(.75)
        self.level_up.set_volume(.75)

        self.board_land_after_clear.set_volume(.75)
        self.clear_line.set_volume(.75)
        self.game_over.set_volume(.75)
        self.game_over_wall.set_volume(.75)
        self.level_up.set_volume(.75)
        self.move_sideways.set_volume(.75)
        self.option_select.set_volume(.75)
        self.pause.set_volume(.75)
        self.rotate.set_volume(.75)
        self.shape_land.set_volume(.75)
        self.switch_option_screen.set_volume(.75)
        self.tetris_clear.set_volume(.75)
