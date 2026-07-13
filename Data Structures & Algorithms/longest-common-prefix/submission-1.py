class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i == len(string) or string[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]  
        return ans   