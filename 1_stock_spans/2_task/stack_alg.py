import sys
sys.path.append('../')

from task_1 import Stack

class Solution():
  def stackStockSpan(self, quotes):
    spans = []
    stack = Stack()
    for index in range(len(quotes)):
      while not stack.isStackIsEmpty() and quotes[stack.top()] <= quotes[index]:
        stack.pop()
      if stack.isStackIsEmpty():
        spans.append(index + 1)
      else:
        spans.append(index - stack.top())
      stack.push(index)

    return spans

