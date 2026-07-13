from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxV = float('-inf')
        temp = deque()
        res = []
        for r in range(len(nums)):
            # Station 1: The Purge (while loop)
            while temp and nums[temp[-1]] < nums[r]:
                temp.pop()

            # Station 2: The Append
            temp.append(r)
            # Station 3: The Eviction (if statement)
            if temp[0] < r - k + 1:
                temp.popleft()

            # Station 4: The Record (if statement)
            if r >= k - 1:
                res.append(nums[temp[0]])
            
        return res

