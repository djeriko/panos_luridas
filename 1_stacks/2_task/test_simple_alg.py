import unittest
import time
from simple_alg import Solution

class TestSolution(unittest.TestCase):
  """
  Should return array with different days
  between stocks prices.
  
  Days
  0 - 1 - 2 - 3 - 4 - 5 - 6
  
  Stock price
  7 - 11 - 8 - 6 - 4 - 8 - 10
  
  Output:
  1 - 2 - 1 - 1 - 1 - 4 - 5
  """
  def testStockSpan(self):
    # arrange
    solution = Solution()
    stocksPrices = [7, 11, 8, 6, 4, 8, 10]
    expected = [1, 2, 1, 1, 1, 4, 5]
    # act
    result = solution.simpleStockSpan(stocksPrices)
    # assert
    self.assertEqual(result, expected)

  def testStockSpanViaStack(self):
    # arrange
    solution = Solution()
    stocksPrices = [7, 11, 8, 6, 4, 8, 10]
    expected = [1, 2, 1, 1, 1, 4, 5]
    # act
    result = solution.simpleStockSpan(stocksPrices)
    # assert
    self.assertEqual(result, expected)
    
    
  def testBigStockSpan(self): 
    # arrange
    startTime = time.time()
    solution = Solution()
    stocksPrices = [
            7, 11, 8, 6, 4, 8, 10, 
            7, 11, 8, 6, 4, 8, 10, 
            7, 11, 8, 6, 4, 8, 10, 
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,

            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            7, 11, 8, 6, 4, 8, 10,
            ]
    expected = [
            1, 2, 1, 1, 1, 4, 5,
            1, 9, 1, 1, 1, 4, 5,
            1, 16, 1, 1, 1, 4, 5,
            1, 23, 1, 1, 1, 4, 5,
            1, 30, 1, 1, 1, 4, 5,
            1, 37, 1, 1, 1, 4, 5,
            1, 44, 1, 1, 1, 4, 5,
            1, 51, 1, 1, 1, 4, 5,
            1, 58, 1, 1, 1, 4, 5,
            1, 65, 1, 1, 1, 4, 5,
            1, 72, 1, 1, 1, 4, 5,
            1, 79, 1, 1, 1, 4, 5,
            1, 86, 1, 1, 1, 4, 5,
            1, 93, 1, 1, 1, 4, 5,

            1, 100, 1, 1, 1, 4, 5,                                              
            1, 107, 1, 1, 1, 4, 5,                                              
            1, 114, 1, 1, 1, 4, 5,                                              
            1, 121, 1, 1, 1, 4, 5,                                              
            1, 128, 1, 1, 1, 4, 5,                                              
            1, 135, 1, 1, 1, 4, 5,                                              
            1, 142, 1, 1, 1, 4, 5,                                              
            1, 149, 1, 1, 1, 4, 5,                                              
            1, 156, 1, 1, 1, 4, 5,                                              
            1, 163, 1, 1, 1, 4, 5,                                              
            1, 170, 1, 1, 1, 4, 5,                                              
            1, 177, 1, 1, 1, 4, 5,                                              
            1, 184, 1, 1, 1, 4, 5,                                              
            1, 191, 1, 1, 1, 4, 5,                                              
            1, 198, 1, 1, 1, 4, 5,                                              
            1, 205, 1, 1, 1, 4, 5,                                              
            1, 212, 1, 1, 1, 4, 5,                                              
            1, 219, 1, 1, 1, 4, 5,                                              
            1, 226, 1, 1, 1, 4, 5,                                              
            1, 233, 1, 1, 1, 4, 5,  
            ]
    # act
    result = solution.simpleStockSpan(stocksPrices)
    # assert
    self.assertEqual(result, expected)
    print("--- %s seconds ---" % (time.time() - startTime))


if __name__ == '__main__':
  unittest.main()
