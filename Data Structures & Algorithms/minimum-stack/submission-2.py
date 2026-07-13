class MinStack:

    def __init__(self):
        self.stackArr = list() 
        self.minEle = float('inf')

    def push(self, val: int) -> None:
        self.stackArr.append(val)
        self.minEle = min(self.minEle, val)

    def pop(self) -> None:
        self.stackArr.pop()
        if self.stackArr:
            self.minEle = min(self.stackArr)
        else:
            self.minEle = float('inf')
        

    def top(self) -> int:
        return self.stackArr[-1]
        

    def getMin(self) -> int:
        return self.minEle

        
