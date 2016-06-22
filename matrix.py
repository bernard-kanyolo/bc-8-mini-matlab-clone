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
        """creates a matrix with all zeros in the specified rows and columns
        creates square matrix if column isn't specified
        """
        if cols is None:
            cols = rows

        data = [[0 for c in range(cols)] for r in range(rows)]
        return cls(data)

    @classmethod
    def ones(cls, rows, cols=None):
        """creates a matrix with all ones in the specified rows and columns
        creates square matrix if column isn't specified
        """
        if cols is None:
            cols = rows

        data = [[1 for c in range(cols)] for r in range(rows)]
        return cls(data)

    @staticmethod
    def scalar_translate(func, matrix):
        """general purpose scalar operations
        takes a function and applies it to every element in the matrix.
        returns the new matrix
        """
        new = [[func(value) for value in matrix.data[index]]
               for index, row in enumerate(matrix.data)]
        return Matrix(new)

    @staticmethod
    def add(matrix1, matrix2):
        """adds matrix2 to matrix1, then returns the new Matrix
        matrices must have the same dimensions
        """
        if (matrix1.rows, matrix1.cols) == (matrix2.rows, matrix2.cols):
            new = [[sum(value) for value in zip(*row)]
                   for row in zip(matrix1.data, matrix2.data)]
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

    @staticmethod
    def subtract(matrix1, matrix2):
        """subtracts matrix2 from matrix1, then returns the new Matrix
        matrices must have the same dimensions
        """
        if (matrix1.rows, matrix1.cols) == (matrix2.rows, matrix2.cols):
            new = [[value[0] - sum(value[1:]) for value in zip(*row)]
                   for row in zip(matrix1.data, matrix2.data)]
            return Matrix(new)
        else:
            raise ValueError("Matrix dimensions must agree")

    @staticmethod
    def transpose(matrix):
        """takes a matrix and returns its transpose, ie. rows and columns switched
        """
        transposed = [list(items) for items in zip(*matrix.data)]
        return Matrix(transposed)

    @staticmethod
    def inverse(matrix):
        """takes a matrix and returns its inverse, if the matrix is square
        uses inv() function from numpy module
        """
        if matrix.cols == matrix.rows:
            return Matrix(inv(matrix.data))
        else:
            raise ValueError("Cannot invert a non-square matrix")

    @staticmethod
    def concat_horizontal(matrix1, matrix2):
        """concatenates matrix2 to matrix1 horizontally together as long as
        they have the same number of rows
        """
        if matrix1.rows == matrix2.rows:
            new = [row + matrix2.data[i] for i, row in enumerate(matrix1.data)]
            return Matrix(new)
        else:
            raise ValueError("Matrices must have same number of rows")

    @staticmethod
    def concat_vertical(matrix1, matrix2):
        """concatenates matrix2 to matrix1 vertically together as long as
        they have the same number of columns
        """
        if matrix1.cols == matrix2.cols:
            new = matrix1.data + matrix2.data
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
            return Matrix.scalar_translate(lambda x: x + other, self)
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
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
to_invert = Matrix([[4, 3], [1, 1]])



a1 = Matrix([[]])
a2 = Matrix([[]])

