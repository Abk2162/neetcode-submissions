class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mys = {}
        myt = {}
        for i in range(len(s)):
            mys[s[i]] = 1 + mys.get(s[i],0)
            myt[t[i]] = 1 + myt.get(t[i],0)
        for c in s:
            if mys[c] != myt.get(c,0):
                return False
        return True