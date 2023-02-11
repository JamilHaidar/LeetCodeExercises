# Leetcode 39

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(candidate_index,chosen_candidates,total_value):
            if total_value>target or candidate_index>=len(candidates):
                return
            if total_value==target:
                result.append(chosen_candidates.copy())
                return
            
            chosen_candidates.append(candidates[candidate_index])
            dfs(candidate_index,chosen_candidates,total_value+candidates[candidate_index])
            chosen_candidates.pop()
            dfs(candidate_index+1,chosen_candidates,total_value)
        dfs(0,[],0)
        return result
    def combinationSum_iterative(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for candidate in candidates:
            for total in range(candidate,target+1):
                if candidate == total:
                    dp[total].append([candidate])
                for elem in dp[total-candidate]:
                    dp[total].append(elem+[candidate])
        return dp[-1]

sol = Solution()

# candidates = [2,3,5]
# target = 8
candidates = [8,6,4,12,5,7,3,11]
target = 28
print(sol.combinationSum(candidates,target))
print(sol.combinationSum_iterative(candidates,target))