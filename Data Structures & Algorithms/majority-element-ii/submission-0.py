class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
            countExtra = count.copy()
            if len(count) > 2:
                for c,n in count.items():
                    if n != 1:
                        countExtra[c] = n - 1
                    else:
                        countExtra.pop(c)
                count = countExtra
        res = []
        for c,n in count.items():
            frequency = nums.count(c)
            if frequency > (len(nums)//3):
                res.append(c)
        return res
