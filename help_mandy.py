import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
   
    while run:
        clock.tick(FPS)
       
        if game.winner() != None:
            print(game.winner())
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
               
            # Ability to use mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(f"Mouse click at position: {pos}, Grid position: ({row}, {col})")
                if game.turn == RED:
                    game.select(row, col)
                   
                elif game.turn == WHITE:
                    game.select(row, col)
           
        game.update()
               
    pygame.quit()
   
main()