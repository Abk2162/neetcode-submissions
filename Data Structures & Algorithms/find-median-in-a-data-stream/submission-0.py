import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.arr[self.length//2] + self.arr[(self.length//2) - 1]) / 2
        else:
            return self.arr[self.length//2]
        
        