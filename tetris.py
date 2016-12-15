import pygame
import ctypes
import platform
import sys
from game_settings import Settings
from block import Block
from shape import Shape
from board import Board
#import game_functions as func

class Tetris():
    """A class representing the game."""

    def __init__(self):
        """Initialize game."""
        pygame.init()

        if platform.system() == 'Windows':
            # Ensure correct screen size to be displayed.
            ctypes.windll.user32.SetProcessDPIAware()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.title_screen = True

        self.current_shape = Shape(self.screen)
        self.next_shape = Shape(self.screen, 600, 520)
        self.board = Board(self.screen)

        # Make a clock object to set fps limit.
        self.clock = pygame.time.Clock()


    def run_game(self):
        """Main function for Tetris."""
        while True:
            # Delta time calculation.
            self.clock.tick(self.settings.fps)

            self.check_events()
            # TODO: Uncomment these lines to show title screen.
            #if self.title_screen:
            #    self.title_screen = func.update_title_screen(self.screen, self.settings)
            #else:
                #func.update_screen(self.screen, self.settings)
            self.update_screen()
            if self.landed:
                self.next_shape.set_position(200,0)
                self.current_shape = self.next_shape
                self.next_shape = Shape(self.screen, 600, 520)

    def update_screen(self):
        """Update everything on screen and then draw the screen."""
        self.draw_board()
        self.landed = self.current_shape.update(self.board)

        if self.landed:
            self.board.add_to_board(self.current_shape)
            self.board.remove_full_lines()
        else:
            self.current_shape.blitme()
        self.next_shape.blitme()
        self.board.blitme()
        pygame.display.update()

        #TODO: ATH, have not modified this function after it was moved from game_functions
    def update_title_screen(screen, settings):
        """Update everything on the title screen, then draw it."""
        screen.blit(settings.title_screen, (0,0))
        display_title_screen = check_events_title_screen()
        pygame.display.update()
        return display_title_screen


    def draw_board(self):
        """Draw everything on the board."""
        self.screen.fill(self.settings.black)
        board_background = pygame.Rect(35, 0, 490, 720)
        pygame.draw.rect(self.screen, self.settings.white, board_background)
        self.screen.blit(self.settings.wall, (40,0))
        self.screen.blit(self.settings.wall, (480,0))
        self.screen.blit(self.settings.scoreboard, (525, 0))


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
            self.current_shape.fall_frequency = 100


    def check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.current_shape.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.current_shape.moving_right = False
        if event.key == pygame.K_DOWN:
            self.current_shape.fall_frequency = 500

    #TODO: ATH, have not modified this function after it was moved from game_functions
    def check_events_title_screen():
        """
        Check for events on title screen and respond to them.
        Returns False if enter key is pressed to stop title_screen.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False
        return True


    def quit_game(self):
        """Quits pygame and python."""
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Tetris().run_game()
