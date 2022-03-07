import sys
sys.path.append('../1_task/')

from task_1 import Stack

"""
Разница стоимостей акций в конкретный день - это число
следующих друг за другом дней, от выбранного нами и в обратном
направлении, до того дня, в который стомость акций была меньше 
или равна стоимости в выбранный на день.
"""
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

