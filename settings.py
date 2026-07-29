"""
    settings.py
    Jack Verdin
    This contains the Settings class, which stores information about how the game works to be accessed by other files.
    7/26/2026
"""
from pathlib import Path
class Settings:
    """Contains settings and values for the working of the game
    """
    def __init__(self):
        """Initializes the class and sets up 'permanent' settings
        """
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'PirateBackground.png'
        self.difficulty_scale = 0.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cannonMobile.png'
        self.ship_w = 30
        self.ship_h = 45

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'cannonBall.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'pirate_ship.png'
        self.alien_w = 40
        self.alien_h = 50
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 40
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """Sets up the 'dynamic' settings
        """
        self.ship_speed_base = 5
        self.ship_speed = self.ship_speed_base
        self.starting_ship_count = 3

        self.bullet_w = 20
        self.bullet_h = 20
        self.bullet_speed_base = 7
        self.bullet_speed = self.bullet_speed_base
        self.bullet_amount = 5

        self.fleet_speed_base = 2
        self.fleet_speed = self.fleet_speed_base
        self.fleet_drop_speed = 40
        self.alien_points_base = 100
        self.alien_points = self.alien_points_base

    def increase_difficulty(self, level):
        """Multiplies the ship, bullet, and fleet speed by a preset difficulty scale
        """
        level -= 1
        self.ship_speed = self.ship_speed_base * (1 + (self.difficulty_scale * level))
        self.alien_points = self.alien_points_base * (1 + (self.difficulty_scale * level))
        self.bullet_speed = self.bullet_speed_base * (1 + (self.difficulty_scale * level))
        self.fleet_speed = self.fleet_speed_base * (1 + (self.difficulty_scale * level))