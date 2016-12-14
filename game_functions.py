import pygame
from block import Block

def update_screen(screen, settings):
    """Update everything on screen and then draw the screen."""
    screen.fill(settings.black)
    
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
