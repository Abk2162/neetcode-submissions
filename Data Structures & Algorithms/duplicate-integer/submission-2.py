class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if not d.get(i):
                d[i]=1
            else:
                return True
        return False