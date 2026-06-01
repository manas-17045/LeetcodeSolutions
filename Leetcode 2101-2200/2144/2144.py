# Leetcode 2144: Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Solved on 1st of June, 2026
class Solution:
    def minimumCost(self, cost: list[int]) -> int:

        cost.sort(reverse=True)
        totalCost = sum(cost) - sum(cost[2::3])

        return totalCost