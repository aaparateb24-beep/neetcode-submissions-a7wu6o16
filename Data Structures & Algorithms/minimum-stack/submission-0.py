class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min stack is empty
        # OR new value is smaller than current minimum
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

        

    def pop(self) -> None:
        # If top element is also minimum
        # remove from both stacks
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        # Return top element
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
