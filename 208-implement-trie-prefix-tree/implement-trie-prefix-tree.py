class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word):
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord("a")] == None:
                curr.children[ord(c) - ord("a")] = TrieNode()
            curr = curr.children[ord(c) - ord("a")]
        curr.isEnd = True

        

    def search(self, word):
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord("a")] == None:
                return False
            curr = curr.children[ord(c) - ord("a")]
        return curr.isEnd
        

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if curr.children[ord(c) - ord("a")] == None:
                return False
            curr = curr.children[ord(c) - ord("a")]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)