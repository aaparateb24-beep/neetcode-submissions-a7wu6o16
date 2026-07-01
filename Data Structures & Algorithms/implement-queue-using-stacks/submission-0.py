class MyQueue:

    def __init__(self):

        # New elements come here
        self.input = []

        # Oldest elements leave from here
        self.output = []

    def push(self, x: int) -> None:

        # Always push into input stack
        self.input.append(x)

    def pop(self) -> int:

        # If output stack is empty,
        # transfer everything.
        if not self.output:

            while self.input:

                # Reverse order
                self.output.append(self.input.pop())

        # Queue front
        return self.output.pop()

    def peek(self) -> int:

        # Prepare output stack if needed
        if not self.output:

            while self.input:

                self.output.append(self.input.pop())

        # Front element
        return self.output[-1]

    def empty(self) -> bool:

        # Queue is empty only if
        # both stacks are empty.
        return len(self.input) == 0 and len(self.output) == 0