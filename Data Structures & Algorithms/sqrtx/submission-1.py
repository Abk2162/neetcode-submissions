class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            mid = ((l+r)//2) 
            mid_sqr = mid * mid
            if mid_sqr > x:
                r = mid - 1
            elif mid_sqr < x:
                l = mid + 1
            else:
                return mid
        return l - 1
            