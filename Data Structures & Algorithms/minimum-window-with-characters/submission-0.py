class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        left, right  = 0,0
        minLength = float('inf')
        l = 0
        check_s = {}
        check_t = {}
        count_s = 0
        for i in t:
           check_t[i] = 1 + check_t.get(i, 0) 
        count_t = len(check_t)

        for r in range(len(s)):
            if s[r] in check_t:
                check_s[s[r]] = 1 + check_s.get(s[r], 0)
                if check_s[s[r]] ==  check_t[s[r]]:
                    count_s += 1
                    while count_s == count_t:
                        if r - l + 1 < minLength:
                            minLength = r - l + 1
                            left = l
                            right = r
                        char_to_remove = s[l]
                        if char_to_remove in check_s:
                            check_s[char_to_remove] -= 1
                            if check_s[char_to_remove] < check_t[char_to_remove]:
                                count_s -= 1
                        l += 1

        if minLength == float('inf'):
            return ""
        return s[left:right+1]
