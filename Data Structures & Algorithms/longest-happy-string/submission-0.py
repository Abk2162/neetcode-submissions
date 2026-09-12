class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(arr, (count, char))
        res = ""
        
        while arr:
            count, val = heapq.heappop(arr)
            if count == 0:
                continue 
            if len(res) >= 2 and res[-1] == res[-2] == val:
                if not arr:
                    return res
                count1, val1 = heapq.heappop(arr)
                res += val1
                if count:
                    heapq.heappush(arr,(count, val))
                if count1+1:
                    heapq.heappush(arr,(count1+1, val1))
                continue 
            res += val
            if count+1:
                heapq.heappush(arr,(count + 1,val))
            
        return res

