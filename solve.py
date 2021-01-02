import numpy as np
import old_board as ob
import gui
import pygame
import random


def works(row, column, board_1, value):
    """returns a boolean on whether a value can work there"""
    temp = board_1[int(row):int(row + 1), :9]
    temp2 = board_1[:9, int(column): int(column + 1)]
    if row < 3:
        if column < 3:
            temp3 = board_1[:3, :3]
        elif column < 6:
            temp3 = board_1[:3, 3:6]
        else:
            temp3 = board_1[:3, 6:9]
    elif row < 6:
        if column < 3:
            temp3 = board_1[3:6, :3]
        elif column < 6:
            temp3 = board_1[3:6, 3:6]
        else:
            temp3 = board_1[3:6, 6:9]
    else:
        if column < 3:
            temp3 = board_1[6:9, :3]
        elif column < 6:
            temp3 = board_1[6:9, 3:6]
        else:
            temp3 = board_1[6:9, 6:9]
    if value in temp:
        return False
    elif value in temp2:
        return False
    elif value in temp3:
        return False
    else:
        return True


def new_board(board, screen, row, column, value):
    screen = gui.update_board(board, screen, row, column, value)
    pygame.display.update()


def backtrack(boards, screen):
    print('backtracking:')
    print(f'board: {boards[-1]}')
    temp = boards[-1]
    temp_board = temp['board']
    print(temp_board)
    boards.pop()

    solve(temp['row'], temp['column'],
          temp_board,
          boards, screen, int(int(temp['value']) + 1.0))


def save_board(row, column, board, boards, screen, value_2):
    print('saved:')

    board[int(row)][int(column)] = value_2
    temp_board = np.copy(board)
    dictionary = {'board': temp_board, 'column': column, 'row': row, 'value': value_2}
    boards.append(dictionary)

    new_board(board, screen, row, column, value_2)
    solve(int(row), int(column + 1), board, boards, screen)


def solve(row, column, board, boards, screen,):
    """solves the sudoku board"""

    if board[8][8] != 0:
        print('hello')
        return True
    else:

        if column == 9.0:
            row = row + 1.0
            column = 0.0
            solve(row, column, board, boards, screen)
        if board[int(row)][int(column)] != 0:
            column = column + 1
            solve(row, column, board, boards, screen)
        for value in range(1, 10):
            if works(row, column, board, value):
                board[int(row)][int(column)] = value
                print(board)
                print(row)
                print(column)

                if solve(row, column, board, boards, screen):
                    print('finished')
                    return True

                board[int(row)][int(column)] = 0

        return False

