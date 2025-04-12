class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            rows, cols, fill_value = args
            if not (isinstance(rows, int) and isinstance(cols, int)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            if not (isinstance(fill_value, (int, float))):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = rows
            self.cols = cols
            self.matrix = [[fill_value for _ in range(cols)] for _ in range(rows)]
        elif len(args) == 1 and isinstance(args[0], list):
            list2D = args[0]
            if not all(isinstance(row, list) for row in list2D):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            if not all(len(row) == len(list2D[0]) for row in list2D):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            if not all(isinstance(x, (int, float)) for row in list2D for x in row):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.rows = len(list2D)
            self.cols = len(list2D[0])
            self.matrix = list2D
        else:
            raise TypeError('неверные аргументы')

    def _check_index(self, row, col):
        if not (isinstance(row, int) and isinstance(col, int)):
            raise IndexError('недопустимые значения индексов')
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def _check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, indices):
        row, col = indices
        self._check_index(row, col)
        return self.matrix[row][col]

    def __setitem__(self, indices, value):
        row, col = indices
        self._check_index(row, col)
        self._check_value(value)
        self.matrix[row][col] = value

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self.matrix[i][j] + other
            return result
        else:
            raise TypeError('операция поддерживается только с матрицами и числами')

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        elif isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols, 0)
            for i in range(self.rows):
                for j in range(self.cols):
                    result[i, j] = self.matrix[i][j] - other
            return result
        else:
            raise TypeError('операция поддерживается только с матрицами и числами')
