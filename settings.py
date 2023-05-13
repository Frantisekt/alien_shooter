class Settings():
	# A Class to store all the Alien invasion parametters. 

	def __init__(self):
		# Initialize the game settings.
		# Screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# Ship settings
		
		self.ship_limits = 3

		# Bullet settings
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Alien setting 
		
		self.fleet_drop_speed = 10

		# How quickly the game speeds up.
		self.speedup_scale = 1.1

		# How quicly the alien point value increases
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Initializes settings that change throughout the game"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.5 # Original 1

		# Fleet direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1
		# Scoring 
		self.alien_points = 50
		
	def increase_speed(self):
		"""Increases speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)

	
