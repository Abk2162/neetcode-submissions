import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        res = []
        temp = []
        for r in range(k):
            temp.append(nums[r])
        res.append(max(temp))
        for r in nums[k:]:
            temp.remove(nums[l])
            l += 1
            temp.append(r)
            res.append(max(temp))
        return res
        

