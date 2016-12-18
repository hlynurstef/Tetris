import pygame
from pygame.time import get_ticks
from pygame.font import Font
from pygame.rect import Rect
import ctypes
import platform
import sys
from music_selection import MusicSelection
from game_settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from utilities import Utilities
from sounds import Sounds
from block import Block
from shape import Shape
from board import Board
from text import Text
from db_conn import DBConnection

class Tetris():
    """A class representing the game."""

    def __init__(self):
        """Initialize game."""
        pygame.mixer.pre_init(44100, 16, 1, 4096)
        pygame.init()

        # Sound Channels.
        self.music_channel = pygame.mixer.Channel(1)


        self.screen = pygame.display.set_mode((800, 720))
        pygame.display.set_caption('Tetris')

        if platform.system() == 'Windows':
            # Ensure correct screen size to be displayed on Windows.
            ctypes.windll.user32.SetProcessDPIAware()


        # Game objects.
        self.settings = Settings()
        self.utils = Utilities(self.settings)
        self.sounds = Sounds()
        self.game_stats = GameStats(self.sounds)
        self.board = Board(self.screen, self.settings, self.sounds)
        self.scoreboard = Scoreboard(self.screen, self.settings, self.game_stats)
        self.music_selection = MusicSelection(self.screen, self.settings, self.sounds, self.music_channel)

        # Tetris shapes.
        self.current_shape = Shape(self.screen, self.settings, self.sounds, self.utils)
        self.next_shape = Shape(self.screen, self.settings, self.sounds, self.utils, 600, 520)

        # Game flags.
        self.title_screen = True
        self.controls_screen = True
        self.select_music_screen = True
        self.game_over = False
        self.high_score_screen = True
        self.show_fps = False
        self.pause = False
        self.music_pause = False

        # Make a clock object to set fps limit.
        self.clock = pygame.time.Clock()

        # Database connection.
        self.db = DBConnection()


    def run_game(self):
        """Main function for Tetris."""

        self.run_title_screen()
        self.run_controls_screen()
        self.run_select_music()
        while True:
            self.run_new_game()
            self.run_game_over()
            self.run_high_score_screen()
            self.music_channel.stop()


    def run_title_screen(self):
        """Run title screen."""
        self.music_channel.play(self.sounds.title_music, -1)
        while self.title_screen:
            self.clock.tick(self.settings.fps)
            self.screen.blit(self.settings.title_screen, (0,0))
            self.check_events_title_screen()
            self.display_fps()
            pygame.display.update()

    def run_controls_screen(self):
        while self.controls_screen:
            self.clock.tick(self.settings.fps)
            self.screen.blit(self.settings.controls_screen, (0,0))
            self.check_events_control_screen()
            self.display_fps()
            pygame.display.update()


    def run_select_music(self):
        """Run option screen for selecting game type and music."""
        self.music_selection.play_music()
        while self.select_music_screen:
            self.clock.tick(self.settings.fps)
            self.screen.blit(self.settings.type_and_music, (0,0))
            self.check_events_select_music()
            self.display_fps()
            self.music_selection.blitme()
            pygame.display.update()


    def run_new_game(self):
        """Run gameplay."""
        if not self.music_channel.get_busy():
            self.music_selection.play_music()
        self.board.clear_board()
        self.game_stats.reset_game_stats()
        self.scoreboard.prep_scoreboard()

        while not self.game_over:
            self.clock.tick(self.settings.fps)

            self.check_events()
            self.update_screen()
            if self.pause:
                self.music_channel.pause()
                self.draw_pause_screen()
                self.music_channel.unpause()

            if self.landed:
                self.next_shape.set_position(200,0)
                self.current_shape = self.next_shape
                self.next_shape = Shape(self.screen, self.settings, self.sounds, self.utils, 600, 520)
                self.game_over = self.board.check_collision(self.current_shape.shape)
                if self.game_over:
                    self.draw_game_over_wall()


    def run_game_over(self):
        """Run game over sreen."""
        self.sounds.game_over.play()
        while self.game_over:
            self.clock.tick(self.settings.fps)
            self.check_events_game_over()
            self.draw_game_over()




    def run_high_score_screen(self):
        """Show highest scores."""
        self.music_channel.stop()
        self.music_channel.play(self.sounds.high_score_music)
        self.db.add_score('player', self.game_stats.score)
        top_ten = self.db.get_top_ten()
        while self.high_score_screen:
            self.clock.tick(self.settings.fps)
            self.check_events_high_score_screen()
            self.screen.blit(self.settings.high_scores, (0,0))
            for row in range(len(top_ten)):
                font = Font(self.settings.font, self.settings.font_size)
                image = font.render('player:' + str(top_ten[row][1]), False, self.settings.black).convert_alpha()
                rect = image.get_rect()
                rect.x = 120
                rect.y = row * 40 + 165
                self.screen.blit(image, rect)
            self.display_fps()
            pygame.display.update()


    def update_screen(self):
        """Update everything on screen and then draw the screen."""
        self.draw_board()
        self.landed = self.current_shape.update(self.board, self.game_stats)

        if self.landed:
            self.board.add_to_board(self.current_shape)
            self.game_stats.set_level_fall_frequency()
            full_lines = self.board.get_full_lines()
            if full_lines:
                self.display_full_lines(full_lines)
                self.board.clear_full_lines(full_lines, self.game_stats)
        else:
            self.current_shape.blitme()

        self.scoreboard.blitme()
        self.next_shape.blitme()
        self.board.blitme()
        self.display_fps()
        pygame.display.update()


    def display_fps(self):
        """Display fps on screen."""
        if self.show_fps:
            pygame.draw.rect(self.screen, self.settings.black, pygame.Rect(0, 0, 80, 40))
            fps_text = Text(self.screen, self.settings, str(int(self.clock.get_fps())), self.settings.white, 80, 0)
            fps_text.blitme()


    def draw_board(self):
        """Draw everything on the board."""
        self.screen.fill(self.settings.black)
        board_background = pygame.Rect(35, 0, 490, 720)
        pygame.draw.rect(self.screen, self.settings.flesh_color, board_background)
        self.screen.blit(self.settings.wall, (40,0))
        self.screen.blit(self.settings.wall, (480,0))
        self.screen.blit(self.settings.scoreboard, (525, 0))


    def draw_game_over_wall(self):
        """Draw the game over wall."""
        self.music_channel.stop()
        self.sounds.game_over_wall.play()

        self.board.fill_row_with_wall(self.settings.board_height-1)
        current_row = self.settings.board_height-2
        self.board.blitme()

        time_of_last_draw = get_ticks()
        draw_time = 50
        while current_row >= 0:
            self.clock.tick(self.settings.fps)
            current_time = get_ticks()
            if current_time - time_of_last_draw > draw_time:
                self.board.fill_row_with_wall(current_row)
                current_row -= 1
                self.board.blitme()
                time_of_last_draw = current_time
            self.display_fps()
            pygame.display.update()
        pygame.time.delay(400)


    def display_full_lines(self, line_indexes):
        """Makes the cleared lines blink."""
        if len(line_indexes) == 4:
            self.sounds.tetris_clear.play()
        else:
            self.sounds.clear_line.play()

        blink_on = True
        blink_time = 250
        blinks = 0
        time_of_last_blink = get_ticks()
        while blinks < 6:
            self.clock.tick(self.settings.fps)
            self.display_fps()
            self.scoreboard.blitme()
            self.next_shape.blitme()
            self.board.blitme()
            current_time = get_ticks()
            if current_time - time_of_last_blink > blink_time:
                blink_on = not blink_on
                time_of_last_blink = current_time
                blinks += 1
            if blink_on:
                for line in line_indexes:
                    pygame.draw.rect(self.screen, self.settings.white, pygame.Rect(80, line * 40, 400, 40))
            pygame.display.update()

        wait = get_ticks() + blink_time
        while current_time < wait:
            current_time = get_ticks()
            self.clock.tick(self.settings.fps)
            self.display_fps()
            self.scoreboard.blitme()
            self.next_shape.blitme()
            self.board.blitme()
            for line in line_indexes:
                pygame.draw.rect(self.screen, self.settings.flesh_color, pygame.Rect(80, line * 40, 400, 40))
            pygame.display.update()
        self.sounds.board_land_after_clear.play()


    def draw_game_over(self):
        """Drawing the game over screen."""
        self.screen.blit(self.settings.game_over, (80,0))
        self.display_fps()
        pygame.display.update()


    def draw_pause_screen(self):
        """Drawing the game over screen."""
        while self.pause:
            self.check_events()
            self.screen.blit(self.settings.pause, (80,0))
            self.display_fps()
            pygame.display.update()


    def check_events(self):
        """Check for events and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self.quit_game()
        if event.key == pygame.K_SPACE:
            self.current_shape.drop = True
            self.current_shape.start_moving_fast()
        if event.key == pygame.K_LEFT:
            self.current_shape.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.current_shape.moving_right = True
        if event.key == pygame.K_UP:
            self.current_shape.rotate(self.board)
        if event.key == pygame.K_DOWN:
            self.game_stats.key_down_fall_frequency()
            self.current_shape.start_moving_fast()
        if event.key == pygame.K_f:
            self.show_fps = not self.show_fps
        if event.key == pygame.K_RETURN:
            self.pause = not self.pause
            self.sounds.pause.play()
        if event.key == pygame.K_m:
            self.pause_music()


    def check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.current_shape.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.current_shape.moving_right = False
        if event.key == pygame.K_DOWN:
            self.game_stats.set_level_fall_frequency()
            self.current_shape.stop_moving_fast()

    def pause_music(self):
        """Pauses music but not effects."""
        if self.music_pause:
            self.music_channel.unpause()
        else:
            self.music_channel.pause()
        self.music_pause = not self.music_pause

    def check_events_title_screen(self):
        """Check for events on title screen and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_f:
                    self.show_fps = not self.show_fps
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.title_screen = False


    def check_events_control_screen(self):
        """Check for events on controls screen and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_f:
                    self.show_fps = not self.show_fps
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.controls_screen = False

    def check_events_select_music(self):
        """Check for events on game type and music screen and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_f:
                    self.show_fps = not self.show_fps
                if event.key == pygame.K_RIGHT:
                    self.music_selection.right()
                if event.key == pygame.K_LEFT:
                    self.music_selection.left()
                if event.key == pygame.K_DOWN:
                    self.music_selection.down()
                if event.key == pygame.K_UP:
                    self.music_selection.up()
                if event.key == pygame.K_RETURN:
                    self.select_music_screen = False


    def check_events_game_over(self):
        """Check for events on game over screen and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_over = False
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_f:
                    self.show_fps = not self.show_fps

    def check_events_high_score_screen(self):
        """Check for events on high score screen and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.high_score_screen = False
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_f:
                    self.show_fps = not self.show_fps

    def quit_game(self):
        """Quits pygame and python."""
        self.db.close_connection()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Tetris().run_game()
