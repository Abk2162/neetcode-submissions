class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for s in strs:
            l = str(len(s))
            sol = sol + l + "#" + s
        return sol

#   3#One3#Two5#Three4#Four4#Five

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1:j+length+1])
            i = j + length + 1

        return strs











