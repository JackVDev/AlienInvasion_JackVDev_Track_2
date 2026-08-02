"""
    alien_fleet.py
    Jack Verdin
    Holds the AlienFleet class, which controls the movement and creation of the enemies
    7/26/2026
"""
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """
        Controls and creates the alien fleet
    """
    def __init__(self, game: 'AlienInvasion'):
        """Initializes an instance of the class

        Args:
            game (AlienInvasion): A link back to the main game
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
    
    def create_fleet(self):
        """Calculates the size of and creates an alien fleet
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        if self.game.game_stats.level % 5 == 0:
            self._create_boss_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)
        else:
            self._create_wave_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Creates a fleet in the shape of a rectangle

        Args:
            alien_w (int): The width of an alien
            alien_h (int): The height of an alien
            fleet_w (int): The total width of the fleet
            fleet_h (int): The total height of the fleet
            x_offset (int): The space between each alien on the x axis
            y_offset (int): The space between each alien on the y axis
        """
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def _create_wave_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Creates a fleet in the shape of a rectangle

        Args:
            alien_w (int): The width of an alien
            alien_h (int): The height of an alien
            fleet_w (int): The total width of the fleet
            fleet_h (int): The total height of the fleet
            x_offset (int): The space between each alien on the x axis
            y_offset (int): The space between each alien on the y axis
        """
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset + (y_offset * ((col-2) % 3) * 0.5)
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def _create_boss_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Creates a large fleet in the shape of a triangle

        Args:
            alien_w (int): The width of an alien
            alien_h (int): The height of an alien
            fleet_w (int): The total width of the fleet
            fleet_h (int): The total height of the fleet
            x_offset (int): The space between each alien on the x axis
            y_offset (int): The space between each alien on the y axis
        """

        for row in range(fleet_h*2):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = (alien_h * row + y_offset) - self.settings.screen_h
                if (col < row) or (col >= fleet_w-row):
                    continue
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Calculates the x and y offsets for the fleet

        Args:
            alien_w (int): The width of an alien
            alien_h (int): The height of an alien
            screen_w (int): The width of the screen
            fleet_w (int): The total width of the fleet
            fleet_h (int): The total height of the fleet

        Returns:
            tuple(int,int): A tuple containing the X Offset and Y Offset for the fleet
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizonal_space = fleet_w * alien_w
        fleet_vetical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizonal_space) // 2)
        y_offset = int((half_screen - fleet_vetical_space) // 2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Calculates the width and height of the fleet

        Args:
            alien_w (int): The width of an alien
            screen_w (_type_): The width of the screen
            alien_h (int): The height of an alien
            screen_h (_type_): The height of the screen

        Returns:
            tuple(int,int): A tuple containing the total width and height of the fleet
        """
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2) // alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)


    def _create_alien(self, current_x: int, current_y: int):
        """Creates a new Alien at the specified coordinates and adds it to the self.fleet attribute

        Args:
            current_x (int): The X coordinate for the new alien
            current_y (int): The Y coordinate for the new alien
        """
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)
    
    def _check_fleet_edges(self):
        """Checks for if the fleet is colliding with the edges, and if so: Drops the fleet down and reverses direction
        """
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Drops the entire fleet down
        """
        alien: Alien
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """Checks the fleet edges, then updates each Alien in the fleet
        """
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        """Calls the draw_alien() method on all aliens in self.fleet
        """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Checks collisions against another sprite group, and destroys any in both that collide

        Args:
            other_group (AbstractGroup): The sprite group to check collisions against

        Returns:
            dict: The key is an item from the first group, and the values are each item in the second group it collides with
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """Checks to see if the fleet has reached the bottom of the screen

        Returns:
            bool: Returns True if the fleet is touching the bottom of the screen, False otherwise
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """Checks for if self.fleet is empty

        Returns:
            bool: True if self.fleet is empty, False otherwise
        """
        return not(self.fleet)