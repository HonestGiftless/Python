# Matrix 🌶️🌶️
class Matrix:
    def __init__(self, rows, cols, value=0) -> None:
        self.rows = rows
        self.cols = cols
        self.value = value
        self._matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __str__(self) -> str:
        result = ''
        for row in range(self.rows):
            result += " ".join(map(str, self._matrix[row]))
            if row != len(self._matrix) - 1:
                result += '\n'

        return result

    def __repr__(self) -> str:
        return f"Matrix({self.rows}, {self.cols})"
    
    def __pos__(self):
        return Matrix(self.rows, self.cols, self.value)
    
    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols, self.value)
        for row in range(self.rows):
            for col in range(self.cols):
                new_matrix.set_value(row, col, -self._matrix[row][col])
        
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows, self.value)
        for row in range(self.cols):
            for col in range(self.rows):
                new_matrix.set_value(row, col, self._matrix[col][row])
        return new_matrix

    def __round__(self, n=None):
        new_matrix = Matrix(self.rows, self.cols, self.value)
        if n is None:
            for row in range(self.rows):
                for col in range(self.cols):
                    new_matrix.set_value(row, col, round(self._matrix[row][col]))
        else:
            for row in range(self.rows):
                for col in range(self.cols):
                    new_matrix.set_value(row, col, round(self._matrix[row][col], n))
        return new_matrix