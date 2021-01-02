import pygame
import numpy as np
import time


def draw(screen):
    pygame.display.set_caption("Sudoku")
    #icon = pygame.image.load('sudoku2.png')
    #pygame.display.set_icon(icon)
    screen.fill((150, 150, 150))

    pygame.draw.line(screen, (0, 0, 0), (0, 50), (450, 50), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (450, 100), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 150), (450, 150), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (450, 200), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 250), (450, 250), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (450, 300), 3)
    pygame.draw.line(screen, (0, 0, 0), (0, 350), (450, 350), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (450, 400), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 450), (450, 450), 3)

    pygame.draw.line(screen, (0, 0, 0), (50, 0), (50, 450), 1)
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 450), 1)
    pygame.draw.line(screen, (0, 0, 0), (150, 0), (150, 450), 3)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 450), 1)
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 450), 1)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 450), 3)
    pygame.draw.line(screen, (0, 0, 0), (350, 0), (350, 450), 1)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 450), 1)
    pygame.draw.line(screen, (0, 0, 0), (450, 0), (450, 450), 3)

    directions_2(screen)

    pygame.display.update()


def update_board(board, screen, row, column, value):
    erase_number(screen, row, column)
    place_number(board, screen, row, column, value)


def erase_number(screen, row, column):
    x_axis = (int(column) * 50) + 20
    y_axis = (int(row) * 50) + 10
    screen.fill((150, 150, 150), (x_axis, y_axis, 28, 28))


def place_number_2(screen, x_position, y_position, value):
    screen.fill((150, 150, 150), (x_position, y_position, 15, 20))
    font = pygame.font.Font(None, 30)
    text = font.render(str(value), 1, (255, 255, 255))
    screen.blit(text, (x_position, y_position))
    pygame.display.update()


def place_number(board, screen, row, column, value):
    x_axis = (int(column) * 50) + 25
    y_axis = (int(row) * 50) + 10
    font = pygame.font.Font(None, 50)
    text = font.render(str(value), 1, (10, 10, 10))
    screen.blit(text, (x_axis, y_axis))
    pygame.display.update()


def place_number_3(screen, x_position, y_position, value):
    screen.fill((150, 150, 150), (x_position, y_position, 22, 30))
    font = pygame.font.Font(None, 50)
    text = font.render(str(value), 1, (25, 67, 255))
    screen.blit(text, (x_position, y_position))
    pygame.display.update()


def quit_game(screen):
    font = pygame.font.Font(None, 75)
    font_2 = pygame.font.Font(None, 40)
    text = font.render('game over', 1, (90, 5, 5))
    text2 = font_2.render('click x button to stop', 1, (90, 5, 5))
    screen.blit(text, (80, 125))
    screen.blit(text2, (30, 225))
    pygame.display.update()
    time.sleep(5)


def directions(screen):
    screen.fill((150, 150, 150), (0, 453, 450, 150))
    font = pygame.font.Font(None, 40)
    text = font.render('press x to stop editing', 1, (60, 150, 5))
    screen.blit(text, (5, 455))


def cursor(x_position, y_position, screen):
    pygame.draw.line(screen, (255, 255, 255), (x_position, y_position),
                     (x_position, y_position + 20), 2)
    pygame.display.update()
    screen.fill((150, 150, 150), (x_position, y_position, 2, 23))
    pygame.display.update()


def cursor_2(x_position, y_position, screen):
    pygame.draw.line(screen, (10, 10, 10), (x_position - 3, y_position),
                     (x_position - 3, y_position + 30), 2)
    pygame.display.update()
    screen.fill((150, 150, 150), (x_position - 3, y_position - 3, 2, 35))
    pygame.display.update()


def directions_2(screen):
    screen.fill((150, 150, 150), (0, 458, 450, 150))
    font = pygame.font.Font(None, 50)
    text = font.render('Press e to edit board', 1, (10, 10, 10))
    text2 = font.render('press space to solve board', 1, (10, 10, 10))
    screen.blit(text, (5, 450))
    screen.blit(text2, (5, 500))
