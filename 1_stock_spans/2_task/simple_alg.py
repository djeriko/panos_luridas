"""
Разница стоимостей акций в конкретный день - это число
следующих друг за другом дней, от выбранного нами и в обратном
направлении, до того дня, в который стомость акций была меньше 
или равна стоимости в выбранный на день.
"""

class Solution():
  def simpleStockSpan(self, quotes):
    spans = []
    for index in range(len(quotes)):
      k = 1
      spanEnd = False
      while index - k >= 0 and not spanEnd:
        if quotes[index - k] <= quotes[index]:
          k = k + 1
        else:
          spanEnd = True
      spans.append(k)

    return spans
