import unittest 
from task_1 import Stack

class TestStack(unittest.TestCase):

  """
  Should add element to top of stack
  """
  def test_stack_push(self):
    stack = Stack()
    stack.push(1)
    self.assertEqual(stack.top(), 1)

  """
  Should remove element from top of stack.
  """
  def test_stack_pop(self):
    stack = Stack()    
    stack.push(1)
    stack.push(2)
    stack.pop()
    self.assertEqual(stack.top(), 1)

  def test_stack_pop_exception(self):
     stack = Stack()
     with self.assertRaises(ValueError):
       stack.pop()

  """
  Should return True when stack is empty.
  """
  def test_is_stack_is_empty(self):
    stack = Stack()
    self.assertTrue(stack.isStackIsEmpty())

  """
  Should return False when stack is filled.
  """
  def test_is_stack_is_not_empty(self):
    stack = Stack()
    stack.push(1)
    self.assertFalse(stack.isStackIsEmpty())

  """
  Should return size of stack.
  """
  def test_stack_size(self):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    self.assertEqual(stack.size(), 3)

  """
  Should return string version of stack.
  [1, 2, 3]
  """
  def test_stack_str(self):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    self.assertEqual(stack.str(), '[1, 2, 3]')

if __name__ == '__main__':
  unittest.main()
      
