# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:11:40 2024

@author: mandy
"""

import pygame
from constants import GREY, SQUARE_SIZE

class Piece:
    PADDING = 15
    OUTLINE = 2
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.col_pos()
            
    def col_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    # Promote piece to a king
    def make_king(self):
        self.king = True
    
    # Create pieces
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            king_radius = radius - 10
            pygame.draw.circle(win, GREY, (self.x, self.y), king_radius)
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.col_pos()
        
    def __repr__(self):
        return str(self.color)