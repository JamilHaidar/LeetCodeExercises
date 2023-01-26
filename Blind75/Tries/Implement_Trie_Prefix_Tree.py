# Leetcode 208

# DICTIONARY IMPLEMENTATION
class Trie:
    # I will use # as an indicator of word end (full word key)
    def __init__(self):
        self.tree = {}
        
    def insert(self, word: str) -> None:
        node = self.tree
        for letter in word:
            node = node.setdefault(letter, {})
        node['#'] = word

    def search(self, word: str) -> bool:
        node = self.tree
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return node.get('#') == word

    def startsWith(self, prefix: str) -> bool:
        node = self.tree
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True

# NODE INDEXING IMPLEMENTATION
# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26
#         self.end = False

# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         current = self.root
#         for character in word:
#             index = ord(character)-ord('a')
#             if current.children[index]:
#                 current = current.children[index]
#             else:
#                 current.children[index] = TrieNode()
#                 current = current.children[index]
#         current.end = True
#     def search(self, word: str) -> bool:
#         current = self.root
#         for character in word:
#             index = ord(character)-ord('a')
#             if current.children[index]:
#                 current = current.children[index]
#             else:
#                 return False
#         return current.end

#     def startsWith(self, prefix: str) -> bool:
#         current = self.root
#         for character in prefix:
#             index = ord(character)-ord('a')
#             if current.children[index]:
#                 current = current.children[index]
#             else:
#                 return False
#         return True



# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))
# print(trie.search("app"))
# print(trie.startsWith("app"))
# trie.insert("app")
# print(trie.search("app"))