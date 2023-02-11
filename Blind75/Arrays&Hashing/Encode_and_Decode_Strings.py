# Leetcode 271

class Solution:
    def encode(self, strs):
        res = ''
        for elem in strs:
            res+=f'{len(elem)}#{elem}'
        return res
    def decode(self, str):
        res = []
        index = 0
        count = 0
        while index<len(str):
            if str[index]=='#':
                res.append(str[index+1:index+count+1])
                index += count+1
                count = 0
                continue
            count = count*10 + int(str[index])
            index+=1
        return res

sol = Solution()
strs = ["we", "say", ":", "yes"]
print(sol.encode(strs))
print(sol.decode(sol.encode(strs)))