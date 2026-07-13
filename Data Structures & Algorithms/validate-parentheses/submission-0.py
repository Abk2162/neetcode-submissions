class Solution:
    def isValid(self, s: str) -> bool:
        open = {'(', '{', '['}
        close = {
            ')':'(',
             '}':'{',
              ']':'['
              }
        stack = []
        for i in s:
            if i in open:
                stack.append(i)
            elif i in close.keys():
                if not stack or close[i] != stack.pop():
                    return False
            else: return False
        if not stack:
            return True
        return False
        
