class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        pre = 1
        for i in range(l):
                res[i] = pre
                pre *= nums[i]
        pos = 1
        for i in range(l):
                j = l - i - 1
                res[j] *= pos
                pos *= nums[j]
        return res