"""
    button.py
    Jack Verdin
    Holds the Button class, which is used to create the Start Button for the main game
    7/26/2026
"""
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """Creates a Button that can be pressed by the player
    """
    def __init__(self, game: 'AlienInvasion', msg):
        """Initializes the class

        Args:
            game (AlienInvasion): A reference back to the main game
            msg (str): The message to be displayed on the Button
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
        self.button_image = pygame.image.load(self.settings.button_file)
        self.button_image = pygame.transform.scale(self.button_image, (self.settings.button_w, self.settings.button_h))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.center = self.boundaries.center
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Prepares the message to be rendered as an image

        Args:
            msg (str): The message to be displayed on the Button
        """
        self.msg_image = self.font.render(msg, True, self.settings.button_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.button_rect.center

    def draw(self):
        """Draws the button to the screen
        """
        self.screen.blit(self.button_image, self.button_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Checks to see if the mouse is on top of the button

        Args:
            mouse_pos (pygame Coordinate): X and Y coordinates of the mouse

        Returns:
            bool: True if the mouse is on the button, False if not
        """
        return self.button_rect.collidepoint(mouse_pos)