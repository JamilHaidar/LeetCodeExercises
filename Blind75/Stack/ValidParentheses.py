# Leetcode 20
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'(','{','['}
        close = {')','}',']'}
        mapping = {')':'(',']':'[','}':'{'}
        for elem in s:
            if elem in open:
                stack.append(elem)
            elif elem in close:
                if len(stack)>0:
                    if stack[-1]==mapping[elem]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack)==0