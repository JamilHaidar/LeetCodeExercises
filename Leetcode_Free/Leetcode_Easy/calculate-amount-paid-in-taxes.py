# Leetcode 2303: Calculate Amount Paid in Taxes
# https://leetcode.com/problems/calculate-amount-paid-in-taxes

from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # tax = 0
        # prev_bracket = 0
        # for bracket in brackets:
        #     if income<=0:break
        #     taxed_dollars = min(income,bracket[0]-prev_bracket)*bracket[1]*0.01
        #     temp = income
        #     income -= bracket[0]-prev_bracket
        #     tax += taxed_dollars
        #     prev_bracket = bracket[0]
        # return tax

        if brackets[0][0]>income: return income*brackets[0][1]*0.01
        tax = 0
        tax += brackets[0][0]*brackets[0][1]*0.01
        for bracket_index in range(1,len(brackets)):
            if income>brackets[bracket_index][0]:
                tax += (brackets[bracket_index][0]-brackets[bracket_index-1][0])*brackets[bracket_index][1]*0.01
            else:
                tax += (income-brackets[bracket_index-1][0])*brackets[bracket_index][1]*0.01
                break
        return tax