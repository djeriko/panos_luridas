import unittest
from rpn import Solution


class TestSolution(unittest.TestCase):
    """
    Should calculate operation -> 1 + (2 x 3)
    writen in Reverse Polish Notation (RPN).
    1 2 3 * +, and return result -> 7.
    """

    def testRPN(self):
        # arrange
        solution = Solution()

        input = ['1', '2', '3', '*', '+']
        # act
        result = solution.rpn(input)

        # assert
        self.assertEqual(result, 7)

    """
    Should calculate operation -> 1 - (4 / 2)
    writen in Reverse Polish Notation (RPN).
    1 4 2 / -, and return result -> - 1.
    """

    def testRPN(self):
        # arrange
        solution = Solution()

        input = ['1', '4', '2', '/', '-']
        # act
        result = solution.rpn(input)

        # assert
        self.assertEqual(result, - 1)


if __name__ == '__main__':
    unittest.main()
