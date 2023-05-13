class GameStats():
	"""Tracks statistics for Alien Invasion."""

	def __init__(self, ai_settings):
		"""Initializes statistics"""
		self.ai_settings = ai_settings
		self.reset_stats()

		# Starts game in an inactive state. 
		self.game_active = False

		# High score should never be resetted.
		self.high_score = 0

	def reset_stats(self):
		"""Initializes statistics that can change during the game"""
		self.ships_left = self.ai_settings.ship_limits
		self.score = 0
		self.level = 1

