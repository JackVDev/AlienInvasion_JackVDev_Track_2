"""
    alien.py
    Jack Verdin
    Holds the Alien class, which controls the properties of individual enemies
    7/26/2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class handling an individual alien

    Args:
        Sprite (pygame Sprite): Details about the sprite
    """
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initializes the class

        Args:
            fleet (AlienFleet): A reference back to the fleet that holds the Alien
            x (float): The x location of the alien
            y (float): The y location of the alien
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Moves the alien based on settings.fleet_speed and fleet_direction
        """
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Checks if the alien is colliding with the edges of the screen

        Returns:
            bool: True if the alien is colliding with the edges, False if not
        """
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
    
    def draw_alien(self):
        """Draws the alien to the screen
        """
        self.screen.blit(self.image, self.rect)