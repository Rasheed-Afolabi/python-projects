class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # High score should never be reset.
        self.high_score = 0
        
        # The game starts in an inactive state.
        self.game_active = False
        # Start Alien Invasion in an active state.
        #self.game_active = True
        
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
        
      
        
        