class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            val1 = heapq.heappop_max(stones)
            val2 = heapq.heappop_max(stones)
            if abs(val1 - val2) != 0:
                heapq.heappush_max(stones, abs(val1 - val2))

        if stones:
            return stones[0]
        else:
            return 0
