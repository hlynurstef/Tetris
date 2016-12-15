import sys
import pygame
from block import Block
from shape import Shape

def update_screen(screen, settings, current_shape, board):
    """Update everything on screen and then draw the screen."""
    draw_board(screen, settings)
    landed = current_shape.update(board)

    if landed:
        board.add_to_board(current_shape)
        board.remove_full_lines()
    board.blitme()

    current_shape.blitme()
    pygame.display.update()
    return landed


def update_title_screen(screen, settings):
    """Update everything on the title screen, then draw it."""
    screen.blit(settings.title_screen, (0,0))
    display_title_screen = check_events_title_screen()
    pygame.display.update()
    return display_title_screen


def draw_board(screen, settings):
    """Draw everything on the board."""
    screen.fill(settings.black)
    board_background = pygame.Rect(35, 0, 490, 720)
    pygame.draw.rect(screen, settings.white, board_background)
    screen.blit(settings.wall, (40,0))
    screen.blit(settings.wall, (480,0))
    screen.blit(settings.scoreboard, (525, 0))


def check_events(shape, board):
    """Check for events and respond to them."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, shape, board)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, shape)


def check_keydown_events(event, shape, board):
    if event.key == pygame.K_ESCAPE:
        quit_game()
    if event.key == pygame.K_LEFT:
        shape.moving_left = True
    if event.key == pygame.K_RIGHT:
        shape.moving_right = True
    if event.key == pygame.K_UP:
        shape.rotate(board)
    if event.key == pygame.K_DOWN:
        shape.fall_frequency = 100


def check_keyup_events(event, shape):
    if event.key == pygame.K_LEFT:
        shape.moving_left = False
    if event.key == pygame.K_RIGHT:
        shape.moving_right = False
    if event.key == pygame.K_DOWN:
        shape.fall_frequency = 500


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

def quit_game():
    """Quits pygame and python."""
    pygame.quit()
    sys.exit()
