import unittest
from matrix import Matrix


class TestMatrixClass(unittest.TestCase):
    """class for Testing whether the Matrix Class functions
    correctly
    """
    @classmethod
    def setUpClass(cls):
        cls.int_matrix = Matrix(1)
        cls.int_matrix_ones = Matrix.ones(1)
        cls.simple_matrix = Matrix([1, 2])
        cls.nested_matrix = Matrix([[1, 2], [3, 4]])
        cls.empty_matrix = Matrix([])
        cls.zeros_two_by_one = Matrix.zeros(2, 1)
        cls.zeros_two_by_two = Matrix.zeros(2)
        cls.ones_two_by_one = Matrix.ones(2, 1)
        cls.ones_two_by_two = Matrix.ones(2)
        cls.to_invert = Matrix([[4, 3], [1, 1]])

    def test_create_matrix_with_int(self):
        """test whether creation of matrix with int is correct
        """
        self.assertListEqual(self.int_matrix.data, [[1]],
                             msg="Matrix(1) should create 1-by-1 matrix")
        self.assertListEqual(self.int_matrix.data, self.int_matrix_ones.data,
                             msg="Matrix(1) should create 1-by-1 matrix")

    def test_create_matrix_with_array(self):
        """test whether initializing the Matrix class
        with an array returns the correct value
        """

        self.assertListEqual(self.simple_matrix.data, [[1, 2]],
                             msg="Matrix should hold [1, 2]")

    def test_create_matrix_with_list_of_list(self):
        """tests whether initializing the Matrix class with list of list
        returns the correct value
        """

        self.assertListEqual(self.nested_matrix.data, [[1, 2], [3, 4]],
                             msg="Nested lists should be added correctly")

    def test_create_matrix_with_empty_list(self):
        """tests whether creating the class with an empty list still works as expected
        """

        self.assertListEqual(
            self.empty_matrix.data, [[]], msg="Matrix([]) should hold [[]]")

    def test_creation_with_zeros_class_method_two_parameters(self):
        """tests whether the 'zeros' constructor works as expected
        """

        self.assertListEqual(self.zeros_two_by_one.data, [[0], [0]],
                             msg="zeros(2,1) should be [[0], [0]]")

    def test_creation_with_zeros_class_method_one_parameter(self):
        """tests whether the 'zeros' constructor works as expected
        """

        self.assertListEqual(self.zeros_two_by_two.data, [[0, 0], [0, 0]],
                             msg="zeros(2) should be [[0, 0], [0, 0]]")

    def test_creation_with_ones_class_method_two_parameters(self):
        """tests whether the 'ones' constructor works as expected
        """

        self.assertListEqual(self.ones_two_by_one.data, [[1], [1]],
                             msg="ones(2,1) should be [[1], [1]]")

    def test_creation_with_ones_class_method_one_parameter(self):
        """tests whether the 'ones' constructor works as expected
        """

        self.assertListEqual(self.ones_two_by_two.data, [[1, 1], [1, 1]],
                             msg="ones(2) should be [[1, 1], [1, 1]]")

    def test_normal_add_matrices(self):
        """tests whether addition of matrices occurs as expected
        """
        self.assertListEqual(self.ones_two_by_two.add(
                             self.ones_two_by_two).data, [[2, 2], [2, 2]])

    def test_different_matrix_dimensions(self):
        """tests whether addition of matrices with different dimensions raises error
        """
        self.assertRaises(ValueError, Matrix.add,
                          self.ones_two_by_two, self.ones_two_by_one)

    def test_sum_of_multiple_matrices(self):
        """tests the sum function in adding an undefined number of matrices
        """
        m = (self.ones_two_by_two, self.ones_two_by_two, self.ones_two_by_two)
        self.assertListEqual(Matrix.sum(*m).data, [[3, 3], [3, 3]])

    def test_normal_subtract_matrices(self):
        """tests whether subtraction of matrices occurs as expected
        """
        self.assertListEqual(self.ones_two_by_two.subtract(
                             self.ones_two_by_two).data, [[0, 0], [0, 0]])

    def test_transpose_normal(self):
        """tests whether transpose works as expected
        """
        self.assertListEqual(self.simple_matrix.transpose().data,
                             [[1], [2]], msg="transpose incorrect")

    def test_concat_horizontal(self):
        """tests combining matrices horizontally
        """
        self.assertListEqual(self.simple_matrix.concat_horizontal(
                             self.simple_matrix).data, [[1, 2, 1, 2]])

    def test_concat_vertical(self):
        """tests combining matrices vertically
        """
        self.assertListEqual(self.simple_matrix.concat_vertical(
                             self.simple_matrix).data, [[1, 2], [1, 2]])

    def test_operator_overloading_plus(self):
        """tests use of '+' operator in addition of matrices
        """
        self.assertListEqual(
            (self.ones_two_by_two + self.ones_two_by_two).data, [[2, 2], [2, 2]])


if __name__ == '__main__':
    unittest.main()
