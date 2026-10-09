class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        num = len(digits)
        res = []
        cur = []
        for i in digits:
            values = digitMap[i]
            if not res:
                res = values
            else:
                cur = []  # Fresh list for this digit!
                for a in values:
                    for b in res:
                        cur.append(b + a)
                res = cur
        return res
                

