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
        print('true')
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


def solve(row, column, board, boards, screen, overide_value=0, ):
    random_number = random.randint(0, 10)
    numbers = []

    temp = board[int(row):int(row + 1), :9]
    temp2 = board[:9, int(column): int(column + 1)]
    if row < 3:
        if column < 3:
            temp3 = board[:3, :3]
        elif column < 6:
            temp3 = board[:3, 3:6]
        else:
            temp3 = board[:3, 6:9]
    elif row < 6:
        if column < 3:
            temp3 = board[3:6, :3]
        elif column < 6:
            temp3 = board[3:6, 3:6]
        else:
            temp3 = board[3:6, 6:9]
    else:
        if column < 3:
            temp3 = board[6:9, :3]
        elif column < 6:
            temp3 = board[6:9, 3:6]
        else:
            temp3 = board[6:9, 6:9]
    """solves the sudoku board"""
    print(f'row: {row} column: {column}')
    print(board)
    if overide_value:
        print('hello')
        print(overide_value)
        if overide_value == 10:
            backtrack(boards, screen)
        else:
            for value in range(overide_value, 10):
                if value not in temp and value not in temp2 and value not in temp3:
                    value_2 = value
                    break
                elif value == 9:
                    if row == 4:
                        boards.pop()
                    if row > 4:
                        boards.pop()
                    if row > 4:
                        boards.pop()
                    #boards.pop()
                    backtrack(boards, screen)
            if value not in temp and value not in temp2 and value not in temp3:
                save_board(row, column, board, boards, screen, value_2)

    elif row == 8.0 and column == 9.0:
        print('finish')
        gui.quit_game(screen)

    elif column == 9.0:
        print('seth')
        row = row + 1.0
        column = 0.0
        solve(row, column, board, boards, screen)

    elif board[int(row)][int(column)] != 0:
        print('annalise')
        solve(int(row), int(column + 1.0), board, boards, screen)

    # else:
    #   print('cool')
    # last_box = board[:3, 6:9]
    # last_box2 = board[3:6, 6:9]
    # last_box3 = board[6:9, 6:9]
    # start = True
    # start_2 = True
    # start_3 = True
    # if range(1, 10) not in last_box:
    #   start = False
    # if range(1, 10) not in last_box2:
    #   start_2 = False
    # if range(1, 10) not in last_box3:
    #   start_3 = False
    # if column < 3 and row < 3 and start:
    #   print('hi')
    #  for number_1 in np.nditer(last_box) and np.nditer(last_box2) and np.nditer(last_box3):
    #     print(number_1)
    #    if number_1 != 0.0:
    #       if last_box not in temp and number_1 not in temp2 and number_1 not in temp3:
    #          value_2 = number_1
    #         save_board(row, column, board, boards, screen, value_2)
    # elif row < 6 and column < 3 and start_2:
    #   for number_1 in np.nditer(last_box2):
    #      if int(number_1) != 0:
    #         if number_1 not in temp and number_1 not in temp2 and number_1 not in temp3:
    #            value_2 = number_1
    #           save_board(row, column, board, boards, screen, value_2)
    # elif column < 3 and start_3:
    #   for number_1 in np.nditer(last_box3):
    #      if int(number_1) != 0:
    #         if number_1 not in temp and number_1 not in temp2 and number_1 not in temp3:
    #            value_2 = number_1
    #           save_board(row, column, board, boards, screen, value_2)
    else:
        for value in range(1, 10):
            if value not in temp and value not in temp2 and value not in temp3:
                value_2 = value
                break
            elif value == 9:
                if row == 5:
                    boards.pop()
                backtrack(boards, screen)
        if value_2 not in temp and value not in temp2 and value not in temp3:
            save_board(row, column, board, boards, screen, value_2)
