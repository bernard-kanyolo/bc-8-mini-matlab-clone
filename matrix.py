class Matrix(object):
    """Class for modelling the basic operations of a Matrix.
    """

    def __init__(self, data):
        """initialize the matrix with nested list
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

