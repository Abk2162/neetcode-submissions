class Node:
    def __init__(self, val = 0, left = None, right = None) :
        self.val = val
        self.left = left
        self.right = right

class MyCircularQueue:
    def __init__(self, k: int):
        self.start = Node()
        self.end = Node()
        self.count = 0
        self.max = k
        self.start.left = self.end
        self.end.right = self.start

        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp = Node(value, self.start.left, self.start)
        self.start.left.right = temp
        self.start.left = temp
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.end.right.right.left = self.end
        self.end.right = self.end.right.right
        self.count -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.end.right.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.start.left.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.max
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()