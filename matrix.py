from numpy.linalg import inv


class Matrix(object):
    """Class for modelling the basic operations of a Matrix.
    """

    def __init__(self, data):
        """initialize the matrix with nested list or normal list
        """
        if len(data) > 0:
            # check if multi-dimensional
            if type(data[0]) == list:
                # check if all rows have same length
                first_length = len(data[0])
                if all(first_length == len(row) for row in data):
                    self.data = data
                else:
                    raise ValueError("All rows must have the same length")
            else:
                self.data = [data]

        else:
            self.data = [[]]

        # set up row and col variables
        self.rows = len(self.data)
        self.cols = 0
        try:
            self.cols = len(self.data[0])
        except IndexError:
            pass

    @classmethod
    def zeros(cls, rows, cols=None):
        """creates a matrix with all zeros in the specified rows and columns.
        creates square matrix if column isn't specified
        """
        if cols is None:
            cols = rows

        data = [[0 for c in range(cols)] for r in range(rows)]
        return cls(data)

    @classmethod
    def ones(cls, rows, cols=None):
        """creates a matrix with all ones in the specified rows and columns.
        creates square matrix if column isn't specified
        """
        if cols is None:
            cols = rows

        data = [[1 for c in range(cols)] for r in range(rows)]
        return cls(data)

    def scalar_translate(self, func):
        """general purpose scalar operations
        takes a function and applies it to every element in the matrix.
        returns the new matrix
        """
        new = [[func(value) for value in self.data[index]]
               for index, row in enumerate(self.data)]
        return Matrix(new)

    def add(self, matrix):
        """adds matrix2 to matrix1, then returns the new Matrix.
        matrices must have the same dimensions
        """
        if (self.rows, self.cols) == (matrix.rows, matrix.cols):
            new = [[sum(value) for value in zip(*row)]
                   for row in zip(self.data, matrix.data)]
            return Matrix(new)
        else:
            raise ValueError("Matrix dimensions must agree")

    @staticmethod
    def sum(*matrices):
        """takes any number of matrices (or ints/floats) and returns a matrix with
        matrix1 + matrix2 + matrix3...
        all matrices must have the same dimensions
        """
        # check for no parameters
        if len(matrices) == 0:
            return [[]]

        first = matrices[0]
        if type(first) == Matrix:
            accumulator = Matrix.zeros(first.rows, first.cols)
        else:
            accumulator = 0

        for matrix in matrices:
            accumulator = accumulator + matrix
        return accumulator

    def subtract(self, matrix):
        """subtracts matrix2 from matrix1, then returns the new Matrix.
        matrices must have the same dimensions
        """
        if (self.rows, self.cols) == (matrix.rows, matrix.cols):
            new = [[value[0] - sum(value[1:]) for value in zip(*row)]
                   for row in zip(self.data, matrix.data)]
            return Matrix(new)
        else:
            raise ValueError("Matrix dimensions must agree")

    def transpose(self):
        """takes a matrix and returns its transpose, ie. rows and columns switched
        """
        transposed = [list(items) for items in zip(*self.data)]
        return Matrix(transposed)

    def inverse(self):
        """takes a matrix and returns its inverse, if the matrix is square.
        uses inv() function from numpy module
        """
        if self.cols == self.rows:
            return Matrix(inv(self.data))
        else:
            raise ValueError("Cannot invert a non-square matrix")

    def concat_horizontal(self, matrix):
        """concatenates matrix to self horizontally together as long as
        they have the same number of rows
        """
        if self.rows == matrix.rows:
            new = [row + matrix.data[i] for i, row in enumerate(self.data)]
            return Matrix(new)
        else:
            raise ValueError("Matrices must have same number of rows")

    def concat_vertical(self, matrix):
        """concatenates matrix to self vertically together as long as
        they have the same number of columns
        """
        if self.cols == matrix.cols:
            new = self.data + matrix.data
            return Matrix(new)
        else:
            raise ValueError("Matrices must have same number of columns")

    def __str__(self):
        """return a string representation when printed or converted
        """
        return str(self.data)

    def __add__(self, other):
        """overload '+' operator for Matrix class
        """
        if type(other) == Matrix:
            return Matrix.add(self, other)
        elif type(other) == int or type(other) == float:
            return self.scalar_translate(lambda x: x + other)
        else:
            return ""

    def __radd__(self, other):
        """same as __add__ except supports reverse ordering
        """
        return Matrix.__add__(self, other)

    def __eq__(self, other):
        """equality for matrix class"""
        return self.data == other.data


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 10, 6], [7, 8, 9]])

print(m2.concat_horizontal(m1).concat_horizontal(m2))
