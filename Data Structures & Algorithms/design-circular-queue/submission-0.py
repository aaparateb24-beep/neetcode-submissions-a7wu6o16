class MyCircularQueue:

    def __init__(self, k: int):
        # -----------------------------------------
        # Create a fixed-size array of size k.
        # Initially every position contains 0.
        # -----------------------------------------
        self.queue = [0] * k

        # -----------------------------------------
        # front -> points to the first element
        #
        # Initially queue is empty, so front starts
        # at index 0.
        # -----------------------------------------
        self.front = 0

        # -----------------------------------------
        # rear -> points to the last inserted element.
        #
        # Initially there is no element,
        # so rear starts at -1.
        # -----------------------------------------
        self.rear = -1

        # -----------------------------------------
        # Current number of elements in the queue.
        # -----------------------------------------
        self.size = 0

        # -----------------------------------------
        # Maximum capacity of the queue.
        # -----------------------------------------
        self.capacity = k

    def enQueue(self, value: int) -> bool:

        # -----------------------------------------
        # Cannot insert if queue is already full.
        # -----------------------------------------
        if self.isFull():
            return False

        # -----------------------------------------
        # Move rear one step ahead.
        #
        # % allows circular movement.
        #
        # Example (capacity = 5):
        #
        # rear = 4
        #
        # (4+1)%5 = 0
        #
        # So rear wraps around to the beginning.
        # -----------------------------------------
        self.rear = (self.rear + 1) % self.capacity

        # -----------------------------------------
        # Insert the new value at rear.
        # -----------------------------------------
        self.queue[self.rear] = value

        # -----------------------------------------
        # One more element is now present.
        # -----------------------------------------
        self.size += 1

        return True

    def deQueue(self) -> bool:

        # -----------------------------------------
        # Cannot remove from an empty queue.
        # -----------------------------------------
        if self.isEmpty():
            return False

        # -----------------------------------------
        # Move front to the next element.
        #
        # Again, % makes it circular.
        #
        # Example:
        #
        # front = 4
        #
        # (4+1)%5 = 0
        # -----------------------------------------
        self.front = (self.front + 1) % self.capacity

        # -----------------------------------------
        # One element has been removed.
        #
        # Note:
        # We don't erase the old value.
        # We simply move front forward.
        # -----------------------------------------
        self.size -= 1

        return True

    def Front(self) -> int:

        # -----------------------------------------
        # No front element if queue is empty.
        # -----------------------------------------
        if self.isEmpty():
            return -1

        # -----------------------------------------
        # Return the element at front.
        # -----------------------------------------
        return self.queue[self.front]

    def Rear(self) -> int:

        # -----------------------------------------
        # No rear element if queue is empty.
        # -----------------------------------------
        if self.isEmpty():
            return -1

        # -----------------------------------------
        # Return the last inserted element.
        # -----------------------------------------
        return self.queue[self.rear]

    def isEmpty(self) -> bool:

        # -----------------------------------------
        # Queue is empty when size becomes 0.
        # -----------------------------------------
        return self.size == 0

    def isFull(self) -> bool:

        # -----------------------------------------
        # Queue is full when current size equals
        # maximum capacity.
        # -----------------------------------------
        return self.size == self.capacity

        































