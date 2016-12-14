import pygame
from block import Block

def update_screen(screen, settings):
    """Update everything on screen and then draw the screen."""
    screen.fill(settings.black)

    # TODO: need to take a look a the positioning of these
    board_background = pygame.Rect(35, 0, 490, 720)
    pygame.draw.rect(screen, settings.white, board_background)
    screen.blit(settings.wall, (40,0))
    screen.blit(settings.wall, (480,0))

    pygame.display.update()


def update_title_screen(screen, settings):
    """Update everything on the title screen, then draw it."""
    screen.blit(settings.title_screen, (0,0))
    display_title_screen = check_events_title_screen()
    pygame.display.update()

    return display_title_screen


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
