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
            if i not in temp.children:
                temp.children[i] = Trie()
            temp = temp.children[i]
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        return temp.end
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        return True
        