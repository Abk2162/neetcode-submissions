class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_items[:k]]