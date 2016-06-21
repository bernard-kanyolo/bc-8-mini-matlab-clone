import unittest
from matrix import Matrix


class TestMatrixClass(unittest.TestCase):
    """class for Testing whether the Matrix Class functions
    correctly
    """

    def test_create_matrix_with_array(self):
        """test whether initializing the Matrix class
        with an array returns the correct value
        """
        simple_matrix = Matrix([1, 2])
        self.assertListEqual(simple_matrix.data, [[1, 2]],
                             msg="Matrix() should hold [1, 2]")

    def test_create_matrix_with_list_of_list(self):
        """tests whether initializing the Matrix class with list of list
        returns the correct value
        """
        nested_matrix = Matrix([[1, 2], [3, 4]])
        self.assertListEqual(nested_matrix.data, [[1, 2], [3, 4]])


if __name__ == '__main__':
    unittest.main()
