class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def __repr__(self):
        return f"Stack({self.stack})"
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())

print(stack.pop())

print(stack.size())

print(stack.is_empty())

print(stack.pop())
print(stack.pop())
print(stack.pop())