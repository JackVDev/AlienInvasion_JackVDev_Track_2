"""
    bullet.py
    Jack Verdin
    Holds the Bullet class which controls the player's projectile and it's functions
    7/26/2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Manages the player's projectile

    Args:
        Sprite (pygame sprite): Details about the sprite
    """
    def __init__(self, game: 'AlienInvasion'):
        """Initializes the class

        Args:
            game (AlienInvasion): A reference back to the main game
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Updates and moves the bullet
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draws the bullet to the screen
        """
        self.screen.blit(self.image, self.rect)