class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        rows = len(matrix)
        if rows == 0:
            return [[]]

        cols = len(matrix[0])

        if not all(map(lambda x: len(x) == cols, matrix)) or \
            not all(map(lambda row: all(map(lambda x: isinstance(x, (int, float)),  row)), matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        h, w = self.size[0], self.size[1]
        sh, sw = self.step[0], self.step[1]

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                res[i][j] = max(s)

        return res

