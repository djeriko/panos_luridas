#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Стек - несложная для реализации структура данных.
# Простейшая ее реализация использует массив; напишите 
# реализацию стека на основе массива. Ранее мы говорили
# о том, что на практике стек имеет куда больше операций,
# возращающие размер стека и проверяющие его наполненность.
# Убедитесь, что для их вы тоже реализовали.
 
class Stack():
  def __init__(self):
    self.stack = []
      
  """ Add element to top of stack. """
  def push(self, i):
    self.stack.append(i)
  
  """ 
  Remove element from top of stack.
  If stack is empty return Exception.
  """
  def pop(self):
    if self.isStackIsEmpty():
      raise ValueError("Stack is empty!")
    self.stack.pop()

  """ 
  Return element from top of stack.
  """
  def top(self):
    return self.stack[-1]

  """ 
  Return true if stack is empty, or
  return false if stack is filled.
  """
  def isStackIsEmpty(self):
    if len(self.stack) > 0:
      return False
    return True

  """
  Return size of stack
  """
  def size(self) -> str:
    return len(self.stack)

  """
  Return string representation of the stack.
  """
  def str(self):
    result = "["
    for i in self.stack: 
      result += str(i) + ", "
    result = result[:-2]  
    result += "]" 
    print(result)
    return result 


    
