"""
    arsenal.py
    Jack Verdin
    Holds the Arsenal class which manages the player's ability to shoot
    7/26/2026
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Holds and manages the player's projectiles, as well as their ability to shoot
    """
    def __init__(self, game: 'AlienInvasion'):
        """Initializes the class

        Args:
            game (AlienInvasion): A reference back to the main game
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
    
    def update_arsenal(self):
        """Updates all active bullets, and removes any that are offscreen
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Removes any bullets that are offscreen
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
    
    def draw(self):
        """Draws every active bullet
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        """Fires a new bullet

        Returns:
            bool: Returns True if successful, False if not
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False