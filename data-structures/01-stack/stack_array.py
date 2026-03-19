class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('Stack is empty.')
            return
        
        item = self.items.pop()
        return item

    def peek(self):
        x = self.items[-1]
        return x
        
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(stack.pop())
    print(stack.peek())
    print(stack.size())