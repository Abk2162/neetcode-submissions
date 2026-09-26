import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            mid_value_hours = 0

            for i in piles:
                mid_value_hours += math.ceil(i/mid)
            
            if mid_value_hours > h:
                l = mid + 1
            else:
                r = mid - 1
            
        return l