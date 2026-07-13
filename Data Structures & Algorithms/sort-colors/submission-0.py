class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rc = wc = bc = pos = 0
        for i in nums:
            if i == 0:
                rc += 1
            elif i == 1:
                wc += 1
            else:
                bc += 1
        wc = rc + wc
        bc = wc + bc
        for i in range(rc):
            nums[i] = 0
        for i in range(rc,wc):
            nums[i] = 1
        for i in range(wc, bc):
            nums[i] = 2   