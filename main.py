#!/usr/bin/env python3

from random import randint
from sys import stdout
from os import system
from tabulate import tabulate


class Game:

    __zero_pos = (3, 3)

    def __init__(self):
        self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def __check_board(self):
        if self.board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
            return True
        else:
            return False

    def __start(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for row_idx, row in enumerate(self.board):
            for column_idx, column in enumerate(self.board[row_idx]):
                if len(numbers) > 1:
                    n = numbers[randint(0, len(numbers)-1)]
                    numbers.remove(n)
                elif len(numbers) == 1:
                    n = numbers[0]
                    numbers.remove(n)
                elif len(numbers) == 0:
                    n = 0

                self.board[row_idx][column_idx] = n

    def show_board(self):
        tab = tabulate(self.board, headers=[
                       "A", "B", "C", "D"], showindex=True, numalign='center', tablefmt='grid')

        print(tab)

    def __check_move(self, pos):
        zero_pos_row, zero_pos_col = self.__zero_pos
        pos_row, pos_col = pos

        if (zero_pos_col == pos_col) or (zero_pos_row == pos_row):
            if (zero_pos_col > pos_col or zero_pos_col < pos_col) or (zero_pos_row > pos_row or zero_pos_row > pos_row):
                return True

    def move(self, direction):
        col = direction[0]
        row = direction[1]

        if col == 'A':
            col = 0
        elif col == 'B':
            col = 1
        elif col == 'C':
            col = 2
        elif col == 'D':
            col = 3

        col, row = int(col), int(row)
        _row, _col = self.__zero_pos

        if self.__check_move((row, col)) is True:
            _tmp = self.board[row][col]
            self.board[row][col] = self.board[_row][_col]
            self.board[_row][_col] = _tmp
            self.__zero_pos = (row, col)

    def main_loop(self):
        self.__start()
        while self.__check_board() is False:
            system('clear')
            self.show_board()
            print('ex.: C3')
            direction = input('>> ')
            self.move(direction)
        print('Congratulations you won!')


g = Game()
g.main_loop()
