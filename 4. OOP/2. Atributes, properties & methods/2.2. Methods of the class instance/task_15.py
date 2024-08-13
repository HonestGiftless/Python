# Класс Knight ♞

import string

class Knight:
    def __init__(self, horizontal, vertical, color) -> None:
        self.horizontal = horizontal.lower()
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return "N"
    
    def can_move(self, col, row):
        a = (string.ascii_lowercase.index(col.lower()) + 1) - (string.ascii_lowercase.index(self.horizontal) + 1)
        b = row - self.vertical

        if a**2 + b**2 == 5:
            return True
        else:
            return False

    def move_to(self, col, row):
        if self.can_move(col, row):
            self.horizontal = col.lower()
            self.vertical = row

    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        x = ord(self.horizontal) - 97
        y = 8 - int(self.vertical)
        board[y][x] = 'N'

        for i in range(8):
            for j in range(8):
                if abs(y - i) * abs(x - j) == 2:
                    board[i][j] = '*'

        for row in board:
            print(*row, sep='')