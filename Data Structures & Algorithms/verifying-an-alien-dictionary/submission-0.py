class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        for i, val in enumerate(order):
            hashmap[val] = i
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]

            for k in range(len(w1)):
                if k == len(w2):
                    return False
                if w1[k] != w2[k]:
                    if hashmap[w1[k]] > hashmap[w2[k]]:
                        return False
                    break


        return True