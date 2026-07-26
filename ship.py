"""
    ship.py
    Jack Verdin
    Holds the Ship class which controls and maintains the Player's Ship
    7/26/2026
"""
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Handles and controls the player ship
    """
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initializes the class

        Args:
            game (AlienInvasion): A reference back to the main game
            arsenal (Arsenal): A reference back to an Arsenal for the ship
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Centers the ship at the midbottom of the screen
        """
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
    
    def update(self):
        """Updates the ship and its arsenal
        """
        # Updating the postition of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Updates the position of the ship
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """Draws the Arsenal and Ship to the screen
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
    
    def fire(self):
        """Attempts to fire a bullet using arsenal.fire_bullet

        Returns:
            bool: True if a bullet was successfully fires, False if not
        """
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """Checks if the ship is colliding with another group of Sprites

        Args:
            other_group (AbstractGroup): The sprite group to check collisions against

        Returns:
            bool: Returns True if the ship is colliding with any of the other sprites, False if not
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        False