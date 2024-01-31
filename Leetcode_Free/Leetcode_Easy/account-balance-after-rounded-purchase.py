# Leetcode 2806: Account Balance After Rounded Purchase
# https://leetcode.com/problems/account-balance-after-rounded-purchase
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount%10>=5:
            return 100-10*((purchaseAmount+5)//10)
        else:
            return 100-10*(purchaseAmount//10)