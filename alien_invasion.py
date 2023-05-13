import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats 
from scoreboard import Scoreboard 
from button import Button

def run_game():
	# Initialize game and creates a screeen object. 
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
	 ai_settings.screen_height)) 
	# Original size 1200:800
	pygame.display.set_caption("Alien Invasion")

	# Makes the Play button. 
	play_button = Button(ai_settings, screen, "Play")

	# Creates an instance to stroce game statistics and creates scoreboards.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Make a ship, a group of aliens and bullets.
	ship = Ship(ai_settings, screen)
	# Make a group to store bullets in. 
	bullets = Group()
	# Makes an Alien.
	aliens = Group()

	# Create a fleete of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Starts the main loop for the game.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, 
			ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb,
			 ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship,
			 aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
		 bullets, play_button)

run_game()