class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]

        for string in strs[1:]:
            while not string.startswith(check):
                check = check[:-1]
        return check  