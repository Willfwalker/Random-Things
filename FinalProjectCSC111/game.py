# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:42:40 2024

@author: mandy
"""

import pygame
from constants import RED, WHITE, BLUE, SQUARE_SIZE
from board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        
    def winner(self):
        return self.board.winner()
        
    def reset(self):
        self._init()
        
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                print(f"Invalid move to ({row}, {col})")
                self.select(row, col)
                return False
            else:
                return True

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            print(f"Piece selected at ({row}, {col}): {piece}")
            return True
        
        print("No piece selected or wrong turn")
        return False
        
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
                self.selected = self.board.get_piece(row, col)
                self.valid_moves = self.board.get_valid_moves(self.selected)
                if self._has_jump_moves():
                    return True
            self.change_turn()
            print(f"Moved piece to ({row}, {col})")
            return True
        else:
            print(f"Move to ({row}, {col}) is invalid")
            
        return False
    
    def _has_jump_moves(self):
        return any(bool(self.valid_moves[move]) for move in self.valid_moves)
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn  == RED:
            self.turn = WHITE
        else:
            self.turn = RED
            print(f"Turn changed to {'WHITE' if self.turn == WHITE else 'RED'}")