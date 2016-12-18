import pygame
import ctypes
import platform
import sys
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


        self.screen = pygame.display.set_mode((800, 720))
        pygame.display.set_caption('Tetris')

        if platform.system() == 'Windows':
            # Ensure correct screen size to be displayed on Windows.
            ctypes.windll.user32.SetProcessDPIAware()

        # Game objects.
        self.settings = Settings()
        self.utils = Utilities(self.settings)
        self.board = Board(self.screen, self.settings)
        self.game_stats = GameStats()
        self.sounds = Sounds()
        self.scoreboard = Scoreboard(self.screen, self.settings, self.game_stats)

        # Tetris shapes.
        self.current_shape = Shape(self.screen, self.settings, self.utils)
        self.next_shape = Shape(self.screen, self.settings, self.utils, 600, 520)

        # Game flags.
        self.title_screen = True
        self.game_over = False
        self.show_fps = False

        # Make a clock object to set fps limit.
        self.clock = pygame.time.Clock()

        # Sound Channel.
        self.channel = pygame.mixer.Channel(1)

        # Database connection.
        self.db = DBConnection()


    def run_game(self):
        """Main function for Tetris."""

        self.run_title_screen()
        while True:
            self.run_new_game()
            self.run_game_over()


    def run_title_screen(self):
        """Run title screen."""
        self.channel.play(self.sounds.title_music, -1)
        while self.title_screen:
            self.clock.tick(self.settings.fps)
            self.update_title_screen()


    def run_new_game(self):
        """Run gameplay."""
        self.channel.stop()
        self.channel.play(self.sounds.a_type_music, -1)
        self.board.clear_board()
        self.game_stats.reset_game_stats()
        self.scoreboard.prep_scoreboard()

        while not self.game_over:
            self.clock.tick(self.settings.fps)

            self.check_events()
            self.update_screen()
            if self.landed:
                self.next_shape.set_position(200,0)
                self.current_shape = self.next_shape
                self.next_shape = Shape(self.screen, self.settings, self.utils, 600, 520)
                self.game_over = self.board.check_collision(self.current_shape.shape)


    def run_game_over(self):
        """Run game over sreen."""
        self.channel.stop()
        self.channel.play(self.sounds.high_score_music, -1)
        while self.game_over:
            self.clock.tick(self.settings.fps)
            self.draw_game_over()
            self.check_events_game_over()
            if self.show_fps:
                self.display_fps()
            pygame.display.update()
        self.db.add_score('player', self.game_stats.score)
        self.db.get_top_ten()

    def update_screen(self):
        """Update everything on screen and then draw the screen."""
        self.draw_board()
        self.landed = self.current_shape.update(self.board, self.game_stats)
        lines_were_cleared = False
        if self.landed:
            self.board.add_to_board(self.current_shape)
            lines_were_cleared = self.board.clear_full_lines(self.game_stats)
        else:
            self.current_shape.blitme()
        self.scoreboard.blitme(lines_were_cleared)
        self.next_shape.blitme()
        self.board.blitme()

        if self.show_fps:
            self.display_fps()
        pygame.display.update()


    def update_title_screen(self):
        """Update everything on the title screen, then draw it."""
        self.screen.blit(self.settings.title_screen, (0,0))
        self.check_events_title_screen()
        if self.show_fps:
            self.display_fps()
        pygame.display.update()


    def display_fps(self):
        """Display fps on screen."""
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


    def update_game_over_screen():
        print("wooohoo")

    def draw_game_over(self):
        """Drawing the game over screen."""
        self.screen.blit(self.settings.game_over, (80,0))



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
        if event.key == pygame.K_LEFT:
            self.current_shape.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.current_shape.moving_right = True
        if event.key == pygame.K_UP:
            self.current_shape.rotate(self.board)
        if event.key == pygame.K_DOWN:
            self.game_stats.key_down_fall_frequency()
        if event.key == pygame.K_f:
            self.show_fps = not self.show_fps


    def check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.current_shape.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.current_shape.moving_right = False
        if event.key == pygame.K_DOWN:
            self.game_stats.set_level_fall_frequency()


    def check_events_title_screen(self):
        """Check for events on title screen and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.title_screen = False
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_f:
                    self.show_fps = not self.show_fps

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


    def quit_game(self):
        """Quits pygame and python."""
        self.db.close_connection()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Tetris().run_game()
