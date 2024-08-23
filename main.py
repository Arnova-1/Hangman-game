import pygame
from src.game.settings import WIDTH, HEIGHT
from src.game.game_loop import GameLoop

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hangman Game")
    
    game = GameLoop(screen)
    game.run()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()