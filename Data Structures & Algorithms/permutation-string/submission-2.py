class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        if len(s2) < l1:
            return False
        l = 0
        check_s1 = {}
        check_s2 = {}
        for i in s1:
            check_s1[i] = 1 + check_s1.get(i, 0)
        for r in range(len(s2)):
            if r - l + 1 > l1:
                check_s2[s2[l]] -= 1
                if check_s2[s2[l]] == 0:
                    del check_s2[s2[l]]
                l += 1
            check_s2[s2[r]] = 1 + check_s2.get(s2[r], 0)
            if check_s1 == check_s2:
                return True
        return False