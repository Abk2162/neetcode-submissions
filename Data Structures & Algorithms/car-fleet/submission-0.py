class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = [(x,y) for x,y in zip(position, speed) ]
        stack = []
        for i,j in sorted(res)[::-1]:
            stack.append((target - i)/j)
            while len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
