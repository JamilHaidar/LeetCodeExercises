# Leetcode 2347: Best Poker Hand
# https://leetcode.com/problems/best-poker-hand
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits_count = Counter(suits)
        rank_count = Counter(ranks)
        if max(suits_count.values())==5:
            return 'Flush'
        if max(rank_count.values())>=3:
            return 'Three of a Kind'
        if max(rank_count.values())==2:
            return 'Pair'
        return 'High Card'