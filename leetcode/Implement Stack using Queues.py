from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()  # Main queue
        self.queue2 = deque()  # Temporary queue

    def push(self, x: int) -> None:
        self.queue1.append(x)  # Always push to queue1

    def pop(self) -> int:
        # Move elements to queue2 except last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        # Last element is the stack's top, so we pop it
        top_element = self.queue1.popleft()

        # Swap queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def top(self) -> int:
        # Move elements to queue2 except last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        # Get the last element (top of stack)
        top_element = self.queue1.popleft()
        self.queue2.append(top_element)  # Put it back to queue2

        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def empty(self) -> bool:
        return len(self.queue1) == 0

# Example Usage:
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())   # Output: 3
print(stack.pop())   # Output: 3
print(stack.empty()) # Output: False
print(stack.pop())   # Output: 2
print(stack.pop())   # Output: 1
print(stack.empty()) # Output: True
