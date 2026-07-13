class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lenArr = len(arr)
        if lenArr == k:
            return arr
        if x >= arr[lenArr-1]:
            return (arr[lenArr-k:lenArr])
        if arr[0] >= x:
            return (arr[0:k])
        l = 0
        r = lenArr - 1
        mid = 0
        res = []
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1   
            else:
                r = mid       
        
        if arr[mid] == x:
            left = mid - 1
            right = mid
        else:
            left = l - 1
            right = l
        while k > 0 and left >= 0  and right < lenArr:
            # if arr[right] == x:
            #     res.add(arr[right])
            #     r += 1
            #     k -= 1
            if x - arr[left] <= arr[right] - x:
                res.append(arr[left])
                left -= 1
                k -= 1
            else:
                res.append(arr[right])
                right += 1
                k -= 1
        while k > 0 and left < 0 and right < lenArr:
            res.append(arr[right])
            right += 1
            k -= 1
        while k > 0 and left >= 0 and right >= lenArr:
            res.append(arr[left])
            left -= 1
            k -= 1

        return sorted(res)