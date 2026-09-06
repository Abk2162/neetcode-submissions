class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in points:
            x,y = i
            dist = ((x**2)+(y**2))
            if len(heap) < k:
                heapq.heappush(heap, (-dist, i))
            else:
                if dist < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, i))
        for j in heap:
            res.append(j[1])
        return res


