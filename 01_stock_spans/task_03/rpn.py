from stack import Stack


class Solution():
    def rpn(self, input):
        stack = Stack()
        for i in input:
            if i == "+":
                a = stack.top()
                stack.pop()
                b = stack.top()
                stack.pop()
                c = int(a) + int(b)
                stack.push(c)
            elif i == "*":
                a = stack.top()
                stack.pop()
                b = stack.top()
                stack.pop()
                c = int(a) * int(b)
                stack.push(c)
            elif i == "-":
                a = stack.top()
                stack.pop()
                b = stack.top()
                stack.pop()
                c = int(a) - int(b)
                stack.push(c)
            elif i == "/":
                a = stack.top()
                stack.pop()
                b = stack.top()
                stack.pop()
                c = int(a) / int(b)
                stack.push(c)
            else:
                stack.push(i)
        return stack.top()
