import pygame
import sys
from typing import List, Tuple, Optional

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 6
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + 400  # Extra space for pieces
WINDOW_HEIGHT = max(GRID_HEIGHT * CELL_SIZE, 600)
COLORS = {
    'F': (255, 0, 0),    # Red
    'I': (0, 255, 0),    # Green
    'L': (0, 0, 255),    # Blue
    'N': (255, 255, 0),  # Yellow
    'P': (255, 0, 255),  # Magenta
    'T': (0, 255, 255),  # Cyan
    'U': (128, 0, 0),    # Dark Red
    'V': (0, 128, 0),    # Dark Green
    'W': (0, 0, 128),    # Dark Blue
    'X': (128, 128, 0),  # Olive
    'Y': (128, 0, 128),  # Purple
    'Z': (0, 128, 128)   # Teal
}

class Pentomino:
    def __init__(self, name: str, shape: List[Tuple[int, int]]):
        self.name = name
        self.shape = shape
        self.rotation = 0
        self.flipped = False
        self.position = (0, 0)
        self.selected = False
        self.placed = False
        
    def rotate(self):
        """Rotate the pentomino 90 degrees clockwise"""
        self.rotation = (self.rotation + 1) % 4
        
    def flip(self):
        """Flip the pentomino horizontally"""
        self.flipped = not self.flipped
        
    def get_current_shape(self) -> List[Tuple[int, int]]:
        """Get the current shape after rotations and flips"""
        shape = self.shape.copy()
        
        # Apply rotation
        for _ in range(self.rotation):
            shape = [(-y, x) for x, y in shape]
            
        # Apply flip
        if self.flipped:
            shape = [(-x, y) for x, y in shape]
            
        return shape

class PentominoGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pentominoes Puzzle")
        
        # Define pentominoes
        self.pentominoes = [
            Pentomino('F', [(0,1), (1,0), (1,1), (1,2), (2,1)]),
            Pentomino('I', [(0,0), (1,0), (2,0), (3,0), (4,0)]),
            Pentomino('L', [(0,0), (1,0), (2,0), (3,0), (3,1)]),
            Pentomino('N', [(0,0), (0,1), (1,1), (1,2), (1,3)]),
            Pentomino('P', [(0,0), (0,1), (1,0), (1,1), (1,2)]),
            Pentomino('T', [(0,0), (1,0), (2,0), (1,1), (1,2)]),
            Pentomino('U', [(0,0), (0,1), (1,1), (2,0), (2,1)]),
            Pentomino('V', [(0,0), (0,1), (0,2), (1,0), (2,0)]),
            Pentomino('W', [(0,0), (1,0), (1,1), (2,1), (2,2)]),
            Pentomino('X', [(1,0), (0,1), (1,1), (2,1), (1,2)]),
            Pentomino('Y', [(0,0), (1,0), (2,0), (3,0), (2,1)]),
            Pentomino('Z', [(0,0), (1,0), (1,1), (2,1), (2,2)])
        ]
        
        # Initialize pentomino positions in the sidebar
        self.arrange_pieces_in_sidebar()
        
        self.selected_piece = None
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        
    def arrange_pieces_in_sidebar(self):
        """Arrange the pentominoes in the sidebar"""
        sidebar_x = GRID_WIDTH * CELL_SIZE + 50
        for i, piece in enumerate(self.pentominoes):
            piece.position = (sidebar_x, 50 + i * (CELL_SIZE * 3))

    def draw_grid(self):
        """Draw the main puzzle grid"""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

    def draw_piece(self, piece: Pentomino):
        """Draw a pentomino piece"""
        shape = piece.get_current_shape()
        color = COLORS[piece.name]
        
        if piece == self.selected_piece:
            # When selected, draw at mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Offset by half the piece size to center on mouse
            base_x = mouse_x - (len(shape) * CELL_SIZE // 2)
            base_y = mouse_y - (len(shape) * CELL_SIZE // 2)
        else:
            # When not selected, draw at piece's stored position
            base_x, base_y = piece.position
        
        for x, y in shape:
            rect = pygame.Rect(
                base_x + (x * CELL_SIZE),
                base_y + (y * CELL_SIZE),
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    def handle_click(self, pos: Tuple[int, int]):
        """Handle mouse clicks"""
        x, y = pos
        
        # Check if click is on a piece in the sidebar
        piece_clicked = False
        for piece in self.pentominoes:
            piece_rect = pygame.Rect(
                piece.position[0],
                piece.position[1],
                CELL_SIZE * 5,
                CELL_SIZE * 5
            )
            if piece_rect.collidepoint(x, y):
                self.selected_piece = piece
                piece_clicked = True
                return

        # If we clicked anywhere else and didn't hit a piece, deselect
        if not piece_clicked:
            self.selected_piece = None

        # If click is on the grid and a piece is selected
        if self.selected_piece and x < GRID_WIDTH * CELL_SIZE:
            grid_x = x // CELL_SIZE
            grid_y = y // CELL_SIZE
            # Attempt to place the piece
            self.try_place_piece(grid_x, grid_y)

    def try_place_piece(self, grid_x: int, grid_y: int):
        """Try to place the selected piece on the grid"""
        if not self.selected_piece:
            return
        
        # Get mouse position and calculate offset to grid
        mouse_x, mouse_y = pygame.mouse.get_pos()
        shape = self.selected_piece.get_current_shape()
        
        # Calculate the grid position taking into account the piece's center offset
        grid_x = (mouse_x - (CELL_SIZE // 2)) // CELL_SIZE
        grid_y = (mouse_y - (CELL_SIZE // 2)) // CELL_SIZE
        
        # Calculate the actual pixel position
        actual_x = grid_x * CELL_SIZE
        actual_y = grid_y * CELL_SIZE
        
        # Update the piece's position
        self.selected_piece.position = (actual_x, actual_y)
        self.selected_piece.placed = True
        
        # Add the piece to the grid
        for x, y in shape:
            grid_pos_x = grid_x + x
            grid_pos_y = grid_y + y
            if 0 <= grid_pos_x < GRID_WIDTH and 0 <= grid_pos_y < GRID_HEIGHT:
                self.grid[grid_pos_y][grid_pos_x] = self.selected_piece.name
        
        self.selected_piece = None

    def run(self):
        """Main game loop"""
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.selected_piece:
                        self.selected_piece.rotate()
                    elif event.key == pygame.K_f and self.selected_piece:
                        self.selected_piece.flip()
            
            # Draw the game
            self.draw_grid()
            
            # Draw all pieces
            for piece in self.pentominoes:
                if piece != self.selected_piece:  # Don't draw selected piece here
                    self.draw_piece(piece)
            
            # Draw the selected piece last (so it appears on top)
            if self.selected_piece:
                self.draw_piece(self.selected_piece)
            
            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PentominoGame()
    game.run() 