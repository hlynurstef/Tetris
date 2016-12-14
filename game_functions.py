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


def check_events():
    """Check for events and respond to them."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()


def quit_game():
    """Quits pygame and python."""
    pygame.quit()
    quit()
