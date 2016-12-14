import pygame
from block import Block

def update_screen(screen, settings, current_shape):
    """Update everything on screen and then draw the screen."""
    draw_board(screen, settings)
    current_shape.update()
    current_shape.blitme()
    pygame.display.update()


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


def check_events():
    """Check for events and respond to them."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()


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
    quit()
