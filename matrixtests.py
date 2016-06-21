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
        self.assertListEqual(nested_matrix.data, [[1, 2], [3, 4]],
                             msg="Nested lists should be added correctly")

    def test_create_matrix_with_empty_list(self):
        """tests whether creating the class with an empty list still works as expected
        """
        empty_matrix = Matrix([])
        self.assertListEqual(
            empty_matrix.data, [[]], msg="Matrix([]) should hold [[]]")

    def test_creation_with_zeros_class_method_two_parameters(self):
        """tests whether the 'zeros' constructor works as expected
        """
        two_by_one = Matrix.zeros(2, 1)
        self.assertListEqual(two_by_one.data, [[0], [0]],
                             msg="zeros(2,1) should be [[0], [0]]")

    def test_creation_with_zeros_class_method_one_parameter(self):
        """tests whether the 'zeros' constructor works as expected
        """
        two_by_two = Matrix.zeros(2)
        self.assertListEqual(two_by_two.data, [[0, 0], [0, 0]],
                             msg="zeros(2) should be [[0, 0], [0, 0]]")

    def test_creation_with_ones_class_method_two_parameters(self):
        """tests whether the 'ones' constructor works as expected
        """
        two_by_one = Matrix.ones(2, 1)
        self.assertListEqual(two_by_one.data, [[1], [1]],
                             msg="ones(2,1) should be [[1], [1]]")

    def test_creation_with_ones_class_method_one_parameter(self):
        """tests whether the 'ones' constructor works as expected
        """
        two_by_two = Matrix.ones(2)
        self.assertListEqual(two_by_two.data, [[1, 1], [1, 1]],
                             msg="ones(2) should be [[1, 1], [1, 1]]")


if __name__ == '__main__':
    unittest.main()
