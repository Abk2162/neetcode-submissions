class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_element = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_element = x

    def pop(self) -> int:
        l = len(self.q)
        for _ in range(l - 1):
            temp = self.q.popleft()
            self.push(temp)
        return self.q.popleft()

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()