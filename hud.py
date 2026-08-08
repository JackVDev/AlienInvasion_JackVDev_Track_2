"""
    hud.py
    Jack Verdin
    Holds the HUD class which is used to display information about the game on the screen for the player
    7/26/2026
"""
import pygame.font
#from alien_invasion import AlienInvasion
#from typing import TYPE_CHECKING

#if TYPE_CHECKING:

class HUD:
    """Contains and controls the User Interface for the game
    """
    def __init__(self, game):
        """Initializes the class

        Args:
            game (AlienInvasion): A reference back to the main game
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.bigfont = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size*2)
        self.smallfont = pygame.font.Font(self.settings.font_file, round(self.settings.HUD_font_size*0.75))
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        """Prepares the image used in redering the life count
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (self.settings.ship_w, self.settings.ship_h))
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):
        """Updates the display for all scores
        """
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self):
        """Updates the Score display
        """
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.bigfont.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        #self.score_rect.right = self.boundaries.right - self.padding
        #self.score_rect.top = self.max_score_rect.bottom + self.padding
        self.score_rect.midtop = (self.boundaries.centerx, self.padding)

    def _update_max_score(self):
        """Updates the Max Score display
        """
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.boundaries.top + self.padding

    def _update_hi_score(self):
        """Updates the High Score display
        """
        hi_score_str = f"High-Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        #self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.score_rect.bottom + self.padding*0)

    def update_level(self):
        """Updates the Level display
        """
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding
        self.update_multiplier()

    def update_multiplier(self):
        """Updates the Point and Difficulty Multiplier display
        """
        multiplier_str = f"Multiplier: {1 + ((self.game_stats.level - 1) * self.settings.difficulty_scale)}x"
        self.multiplier_image = self.smallfont.render(multiplier_str, True, self.settings.text_color, None)
        self.multiplier_rect = self.multiplier_image.get_rect()
        self.multiplier_rect.midtop = self.level_rect.midbottom

    def _draw_lives(self):
        """Draws the life counter to the screen
        """
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """Draws all displays to the screen
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.multiplier_image, self.multiplier_rect)
        self._draw_lives()

    def game_over_scores(self):
        """Updates the score counters to a different position for when the game is not active
        """

        hi_score_str = f"High-Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.bigfont.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding*3)

        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.bigfont.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = (self.boundaries.centerx, self.hi_score_rect.bottom + self.padding*2)

        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.midtop = (self.score_rect.centerx, self.score_rect.bottom + self.padding*0)

        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midtop = (self.max_score_rect.centerx, self.max_score_rect.bottom + self.padding*0)
        self.update_multiplier()