class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        seating = 0
        heap = []
        for i in trips:
            people, start, stop = i
            heapq.heappush(heap, (start,'1getpeople', people, stop))
        while heap:
            if heap:
                if heap[0][1] == '1getpeople':
                    cur_s, _  , cur_p, cur_stop = heapq.heappop(heap)
                    if seating + cur_p > capacity:
                        return False
                    seating += cur_p
                    heapq.heappush(heap, (cur_stop, '0pushpeople', cur_p))
                if heap[0][1] == '0pushpeople':
                    cur_stop, _, cur_p = heapq.heappop(heap)
                    seating -= cur_p
        return True