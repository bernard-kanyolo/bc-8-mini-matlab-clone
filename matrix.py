class Matrix(object):
    """Class for modelling the basic operations of a Matrix.
    """

    def __init__(self, data):
        """initialize the matrix with nested list or normal list
        """
        if len(data) > 0:

            if type(data[0]) == list:
                if all(len(data[0]) == len(row) for row in data):
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
