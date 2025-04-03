class Solution(object):

    class TrieNode:
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26

    def longestWord(self, words):
        root = self.TrieNode()

        def insert(word):
            curr = root
            for c in word:
                if curr.children[ord(c) - ord("a")] == None:
                    curr.children[ord(c) - ord("a")] = self.TrieNode()
                curr = curr.children[ord(c) - ord("a")]
            curr.isEnd = True

        for word in words:
            insert(word)

        def dfs(root, path):
            # base case: if we reach the end of the trie or can't go deeper
            current_word = "".join(path)
            result = current_word

            # check if this word is the longest word so far
            if len(path) > len(result):
                result = current_word
            elif len(path) == len(result):
                result = min(result, current_word)

            # explore deeper in the trie
            for i in range(26):
                curr = root.children[i]
                if curr and curr.isEnd:
                    path.append(chr(i + ord("a")))
                    deeper_result = dfs(curr, path)  # Recursively call dfs
                    if len(deeper_result) > len(result):
                        result = deeper_result
                    path.pop()

            return result
        
        # start dfs from root
        return dfs(root, [])
