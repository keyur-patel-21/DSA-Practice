class Solution(object):
    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26

    def replaceWords(self, dictionary, sentence):
        root = self.TrieNode()

        def insert(word):
            curr = root
            for c in word:
                if curr.children[ord(c) - ord("a")] == None:
                    curr.children[ord(c) - ord("a")] = self.TrieNode()
                curr = curr.children[ord(c) - ord("a")]
            curr.isEnd = True

        for word in dictionary:
            insert(word)

        sen_words = sentence.split(" ")

        result = []

        def getShortest(word):
            curr = root
            shortest = ""
            for c in word:
                if curr.children[ord(c) - ord("a")] == None or curr.isEnd == True:
                    break
                curr = curr.children[ord(c) - ord("a")]
                shortest += c

            if curr.isEnd == True:
                return shortest
            return word


        for word in sen_words:
            result.append(getShortest(word))

        return " ".join(result)

         

        

        
        