class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                vol = (min(heights[i], heights[j])*abs(i-j))
                max_val = max(vol, max_val)
        return max_val