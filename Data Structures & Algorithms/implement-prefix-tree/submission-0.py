class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if i in temp.children:
                temp = temp.children[i]
                continue
            else:
                new = Trie(i)
                temp.children[i] = new
                temp = new
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        if temp.end == False:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        return True
        