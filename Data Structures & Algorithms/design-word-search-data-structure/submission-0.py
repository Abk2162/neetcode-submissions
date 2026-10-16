class Trie:
    def __init__(self, val=None):
        self.val = val
        self.children = dict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        temp = self.root
        for i in word:
            if i not in temp.children:
                temp.children[i] = Trie()
            temp = temp.children[i]
        temp.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if len(word) == i:
                return node.end
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]],i+1)
        return dfs(self.root,0)



