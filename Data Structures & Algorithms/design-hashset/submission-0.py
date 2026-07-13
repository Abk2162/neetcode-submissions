class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
 
class MyHashSet:
 
    def __init__(self):
        self.arr = [Node(0) for i in range(10000)]

    def add(self, key: int) -> None:
        pos = self.arr[key % 10000]
        while pos.next:
            if pos.next.val == key:
                return
            pos = pos.next
        pos.next = Node(key)

    def remove(self, key: int) -> None:
        pos = self.arr[key % 10000]
        while pos.next:
            if pos.next.val == key:
                pos.next = pos.next.next
                return
            pos = pos.next

    def contains(self, key: int) -> bool:
        pos = self.arr[key % 10000]
        while pos.next:
            if pos.next.val == key:
                return True
            pos = pos.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)