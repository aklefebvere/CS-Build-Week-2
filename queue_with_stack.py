# probably implemented wrong
class MyQueue:

    def __init__(self):
        self.size = 0
        self.storage = []
        

    def push(self, x: int) -> None:
        self.storage.append(x)
        self.size += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1
        return self.storage.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size == 0:
            return True
