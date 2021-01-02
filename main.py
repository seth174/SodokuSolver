import numpy as np
import solve as s
import old_board as ob
import pygame
import gui
from pygame.locals import *
import time
import sys

board = np.zeros((9, 9))
board[0][0] = 0
board[0][4] = 0
board[0][5] = 0
board[0][6] = 0
board[0][7] = 0
board[1][3] = 0
board[1][4] = 0
board[1][5] = 0
board[1][7] = 0
board[2][1] = 0
board[2][7] = 0
board[3][7] = 0
board[3][8] = 0
board[4][0] = 0
board[4][1] = 0
board[4][7] = 0
board[4][8] = 0
board[5][0] = 0
board[5][1] = 0
board[6][1] = 0
board[6][7] = 0
board[7][1] = 0
board[7][3] = 0
board[7][4] = 0
board[7][5] = 0
board[8][1] = 0
board[8][2] = 0
board[8][3] = 0
board[8][4] = 0
board[8][8] = 0
boards = []
new_solve = s.Solve(board)
pygame.init()
screen = pygame.display.set_mode((450, 600))
gui.draw(screen=screen)
for value in range(0, 9):
    for value_2 in range(0, 9):
        gui.place_number(board, screen, value, value_2, int(board[value][value_2]))
pygame.display.update()

running = True
running_2 = True

y_axis = 5
x_axis = 5

y_axis_2 = 10
x_axis_2 = 25

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                new_solve.solve(row=0, column=0, screen=screen,
                                boards=boards, )
            elif event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_UP:
                if y_axis != 5:
                    y_axis = y_axis - 50
            elif event.key == pygame.K_DOWN:
                if y_axis != 405:
                    y_axis = y_axis + 50
            elif event.key == pygame.K_LEFT:
                if x_axis != 5:
                    x_axis = x_axis - 50
            elif event.key == pygame.K_RIGHT:
                if x_axis != 405:
                    x_axis = x_axis + 50
            elif event.key == pygame.K_1:
                gui.place_number_2(screen, x_axis, y_axis, 1)
            elif event.key == pygame.K_2:
                gui.place_number_2(screen, x_axis, y_axis, 2)
            elif event.key == pygame.K_3:
                gui.place_number_2(screen, x_axis, y_axis, 3)
            elif event.key == pygame.K_4:
                gui.place_number_2(screen, x_axis, y_axis, 4)
            elif event.key == pygame.K_5:
                gui.place_number_2(screen, x_axis, y_axis, 5)
            elif event.key == pygame.K_6:
                gui.place_number_2(screen, x_axis, y_axis, 6)
            elif event.key == pygame.K_7:
                gui.place_number_2(screen, x_axis, y_axis, 7)
            elif event.key == pygame.K_8:
                gui.place_number_2(screen, x_axis, y_axis, 8)
            elif event.key == pygame.K_9:
                gui.place_number_2(screen, x_axis, y_axis, 9)
            elif event.key == pygame.K_e:
                gui.directions(screen)
                pygame.display.update()
                running_2 = True
                while running_2:
                    for event_2 in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            running_2 = False
                        elif event_2.type == pygame.KEYDOWN:
                            if event_2.key == pygame.K_x:
                                running_2 = False
                                gui.directions_2(screen)
                            elif event_2.key == pygame.K_0:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 0)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 0
                            elif event_2.key == pygame.K_1:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 1)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 1
                            elif event_2.key == pygame.K_2:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 2)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 2
                            elif event_2.key == pygame.K_3:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 3)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 3
                            elif event_2.key == pygame.K_4:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 4)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 4
                            elif event_2.key == pygame.K_5:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 5)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 5
                            elif event_2.key == pygame.K_6:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 6)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 6
                            elif event_2.key == pygame.K_7:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 7)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 7
                            elif event_2.key == pygame.K_8:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 8)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 8
                            elif event_2.key == pygame.K_9:
                                gui.place_number_3(screen, x_axis_2, y_axis_2, 9)
                                board[int(y_axis_2 / 50)][int(x_axis_2 / 50)] = 9
                            elif event_2.key == pygame.K_UP:
                                if y_axis_2 != 10:
                                    y_axis_2 = y_axis_2 - 50
                            elif event_2.key == pygame.K_DOWN:
                                if y_axis_2 != 410:
                                    y_axis_2 = y_axis_2 + 50
                            elif event_2.key == pygame.K_LEFT:
                                if x_axis_2 != 25:
                                    x_axis_2 = x_axis_2 - 50
                            elif event_2.key == pygame.K_RIGHT:
                                if x_axis_2 != 425:
                                    x_axis_2 = x_axis_2 + 50
                    gui.cursor_2(x_axis_2, y_axis_2, screen)

    gui.cursor(x_axis, y_axis, screen)

new_solve.solve(row=0, column=0, screen=screen,
                boards=boards, )

