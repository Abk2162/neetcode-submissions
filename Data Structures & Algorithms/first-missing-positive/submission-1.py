class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        hashSet = set(nums)
        for i in range(1,n+1):
            if i not in hashSet:
                return i
        return n + 1
