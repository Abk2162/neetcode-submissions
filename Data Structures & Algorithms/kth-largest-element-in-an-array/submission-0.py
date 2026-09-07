class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [nums[0]]
        for i in nums[1:]:
            if len(heap) < k:
                heapq.heappush(heap, i)
            elif i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        return heap[0]
            