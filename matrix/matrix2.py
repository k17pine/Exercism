import numpy as np


class Matrix:
    def __init__(self, matrix_string):
        self.col = [0]
        self.rows = [0]
        for columns in matrix_string.splitlines():
            self.col.append(list(map(int, columns.split())))
        for i in range(1, len(self.col)):
            if i == 1:
                for j in self.col[i]:
                    self.rows.append([j])
            else:
                for m in range(1, len(self.col[i])+1):
                    self.rows[m].append(self.col[i][m-1])

    def row(self, index):
        return self.col[index]

    def column(self, index):
        return self.rows[index]

#matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")