# Leetcode 212

from typing import List

# First approach: Build a Trie with word removal

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False
        self.word_count = 0

class Trie:    
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self,word:str) -> None:
        current_node = self.root
        current_node.word_count+=1
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode()
            current_node = current_node.children[letter]
            current_node.word_count+=1
        current_node.end = True

    def search(self,word:str) -> bool:
        current_node = self.root
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False
        return current_node.end
    
    def remove(self,word:str) -> None:
        current_node = self.root
        current_node.word_count-=1
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
                current_node.word_count -=1
        current_node.end = False
class Solution:
    
    def print_trie(self):
        temp = self.trie.root
        stack = [[temp,'']]
        while stack:
            node,word_so_far = stack.pop()
            print(word_so_far,node.children.keys(),node.end)
            for key in node.children:
                stack.append([node.children[key],word_so_far+key])
        print()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.result = []

        self.dx = [-1,1,0,0]
        self.dy = [0,0,1,-1]

        self.visited = set()
        
        def dfs(row_idx:int,col_idx:int,current_node:TrieNode,word_so_far:str):
            within_borders = row_idx>-1 and row_idx<len(board) and col_idx>-1 and col_idx<len(board[row_idx])
            if not within_borders: return
            if board[row_idx][col_idx] not in current_node.children:
                return
            if current_node.word_count<1:
                return
            if (row_idx,col_idx) in self.visited:
                return
            
            self.visited.add((row_idx,col_idx))
            current_node = current_node.children[board[row_idx][col_idx]]
            word_so_far = word_so_far + board[row_idx][col_idx]
            if current_node.end:
                self.trie.remove(word_so_far)
                self.result.append(word_so_far)
            
            for direction in range(4):
                new_row_idx = row_idx+self.dy[direction]
                new_col_idx = col_idx+self.dx[direction]
                dfs(new_row_idx,new_col_idx,current_node,word_so_far)

            self.visited.remove((row_idx,col_idx))

        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                dfs(row_idx,col_idx,self.trie.root,'')
        return self.result
# # Second approach: DFS on board (brute force)
# class Solution:
    
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         self.board = board
#         self.words = set(words)
#         self.dx = [-1,1,0,0]
#         self.dy = [0,0,1,-1]

#         self.visited = [[False for _ in board[0]] for _ in board]
#         self.res = set()
#         for row_idx in range(len(board)):
#             for col_idx in range(len(board[row_idx])):
#                 self.dfs(row_idx,col_idx,str(board[row_idx][col_idx]))
#         return list(self.res)

#     def dfs(self,row_idx,col_idx,to_find) -> None:
#         if to_find in self.words:
#             self.res.add(to_find)
#         self.visited[row_idx][col_idx] = True
#         for direction in range(4):
#             new_row_idx = row_idx+self.dy[direction]
#             new_col_idx = col_idx+self.dx[direction]
            
#             within_borders = new_row_idx>-1 and new_row_idx<len(board) and new_col_idx>-1 and new_col_idx<len(board[row_idx])
#             if within_borders and not self.visited[new_row_idx][new_col_idx]:
#                 self.dfs(new_row_idx,new_col_idx,to_find+board[new_row_idx][new_col_idx])
#         self.visited[row_idx][col_idx] = False

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# board = [['a','a']]
# words = ['a']
# board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
# words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

sol = Solution()
print(sol.findWords(board,words))