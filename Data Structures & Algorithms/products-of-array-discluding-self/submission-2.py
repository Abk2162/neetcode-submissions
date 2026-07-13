class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        flag = 0
        for i in nums:
            if i == 0:
                flag += 1
            else:
                totalProd *= i


        for i in range(len(nums)):
            if flag > 1:
                nums[i] = 0
            elif flag == 1:
                if nums[i] == 0:
                    nums[i] = totalProd
                else:
                    nums[i] = 0
            else:
                if nums[i] != 0:
                    nums[i] = totalProd // nums[i]
        return nums
 