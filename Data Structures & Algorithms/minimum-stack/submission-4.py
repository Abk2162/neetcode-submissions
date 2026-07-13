class MinStack:

    def __init__(self):
        self.stackArr = list()

    def push(self, val: int) -> None:
        
        if self.stackArr:
            minEle = min(val, self.stackArr[-1][1])
        else:
            minEle = val
        self.stackArr.append((val, minEle))
        

    def pop(self) -> None:
        self.stackArr.pop()
        
        

    def top(self) -> int:
        return self.stackArr[-1][0]
        

    def getMin(self) -> int:
        return self.stackArr[-1][1]
        
