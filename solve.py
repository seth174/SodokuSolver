import numpy as np
import old_board as ob
import gui
import pygame
import random


class Solve:
    endSolve = False

    def __init__(self, board):
        self.board = board

    def works(self, row, column, value):
        """returns a boolean on whether a value can work there"""
        temp = self.board[int(row):int(row + 1), :9]
        temp2 = self.board[:9, int(column): int(column + 1)]
        if row < 3:
            if column < 3:
                temp3 = self.board[:3, :3]
            elif column < 6:
                temp3 = self.board[:3, 3:6]
            else:
                temp3 = self.board[:3, 6:9]
        elif row < 6:
            if column < 3:
                temp3 = self.board[3:6, :3]
            elif column < 6:
                temp3 = self.board[3:6, 3:6]
            else:
                temp3 = self.board[3:6, 6:9]
        else:
            if column < 3:
                temp3 = self.board[6:9, :3]
            elif column < 6:
                temp3 = self.board[6:9, 3:6]
            else:
                temp3 = self.board[6:9, 6:9]
        if value in temp:
            return False
        elif value in temp2:
            return False
        elif value in temp3:
            return False
        else:
            return True

    def solve(self, row, column, boards, screen, end=False):
        """solves the sudoku board"""

        if column == 8 and row == 8:
            Solve.endSolve = True
            return True
        elif Solve.endSolve:
            return True
        else:

            if column == 9.0:
                row = row + 1.0
                column = 0.0
                self.solve(row, column, boards, screen)
            if self.board[int(row)][int(column)] != 0:
                column = column + 1
                self.solve(row, column, boards, screen)
            for value in range(1, 10):
                if self.works(row, column, value):
                    gui.update_board(self.board, screen, row, column, value)
                    self.board[int(row)][int(column)] = value
                    print(self.board)
                    print(row)
                    print(column)

                    if self.solve(row, column, boards, screen):
                        end = True
                        return True

                    self.board[int(row)][int(column)] = 0

            return False
