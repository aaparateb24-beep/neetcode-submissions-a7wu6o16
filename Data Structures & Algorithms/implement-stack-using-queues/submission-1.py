from collections import deque

class MyStack:

    def __init__(self):

        # Queue
        self.q = deque()

    def push(self, x):

        # Add new element
        self.q.append(x)

        # Rotate all previous elements
        #
        # Example:
        #
        # Before:
        # 1 2
        #
        # After:
        # 2 1
        for _ in range(len(self.q)-1):

            self.q.append(self.q.popleft())

    def pop(self):

        # Front behaves like stack top
        return self.q.popleft()

    def top(self):

        return self.q[0]

    def empty(self):

        return len(self.q)==0