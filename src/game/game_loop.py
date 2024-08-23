import pygame
from src.game.settings import FPS
from src.utils.constant import BACKGROUND

class GameLoop:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
    
    def run(self):
        while self.running:
            self._handle_events()
            self._draw()
            self.clock.tick(FPS)
            
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def _draw(self):
        self.screen.fill(BACKGROUND)
        pygame.display.flip()        