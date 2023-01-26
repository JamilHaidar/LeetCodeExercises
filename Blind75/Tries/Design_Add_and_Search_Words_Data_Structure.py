# Leetcode 211
# DICTIONARY IMPLEMENTATION
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
        current_node.word = True

    def search(self, word: str) -> bool:
        def dfs(letter_index, root):
            current_node = root
            for i in range(letter_index,len(word)):
                letter = word[i]
                if letter == '.':
                    for child in current_node.children.values():
                        if dfs(i+1,child):return True
                else:
                    if letter not in current_node.children:return False
                    current_node =current_node.children[letter]
            return current_node.word

        return dfs(0, self.root)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True