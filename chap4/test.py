# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.top = None

    def peek(self):
        if self.top:
            return self.top.value
        return None

    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.prev
            return node.value
        return None

    def push(self, number):
        self.top = Node(number, self.top)

    def getMin(self):
        if self.top:
            return self.top.min
        return None

    def getMax(self):
        if self.top:
            return self.top.max
        return None


class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        self.min, self.max = value, value
        if prev:
            if value > prev.min:
                self.min = prev.min
            if value < prev.max:
                self.max = prev.max

stack = MinMaxStack()
stack.push(5)
print(stack.peek())
stack.push(7)
print(stack.peek())
stack.push(2)
print(stack.peek())
print('min: ' + str(stack.getMin()))
print('max: ' + str(stack.getMax()))
print('pop: ' + str(stack.pop()))
print(stack.peek())
