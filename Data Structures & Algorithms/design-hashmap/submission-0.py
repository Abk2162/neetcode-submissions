class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        

class MyHashMap:

    def __init__(self):
        self.arr = [Node(-1,-1) for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        pos = self.arr[key % 10000]
        while pos.next:
            if pos.next.key == key:
                pos.next.val = value
                return
            pos = pos.next
        pos.next = Node(key, value)

    def get(self, key: int) -> int:
        pos = self.arr[key % 10000]
        while pos.next:
            if pos.next.key == key:
                return pos.next.val
            pos = pos.next
        return -1

    def remove(self, key: int) -> None:
        pos = self.arr[key % 10000]
        while pos.next:
            if pos.next.key == key:
                pos.next = pos.next.next
                return
            pos = pos.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)