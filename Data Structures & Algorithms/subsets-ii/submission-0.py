class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
             
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        unique_tuples = set(tuple(sublist) for sublist in res)

        unique_lists = [list(t) for t in unique_tuples]
        return unique_lists