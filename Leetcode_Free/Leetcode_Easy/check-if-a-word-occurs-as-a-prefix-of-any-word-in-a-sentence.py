# Leetcode 1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index,word in enumerate(sentence.split()):
            if len(word)<len(searchWord):continue
            if searchWord == word[:len(searchWord)]:
                return index + 1
        return -1