class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        median = len(nums) // 2
        return nums[median]