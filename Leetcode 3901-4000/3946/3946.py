# Leetcode 3946: Maximum Number of Items From Sale I
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
# Solved on 14th of June, 2026
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        """
        Calculates the maximum number of items that can be obtained within a given budget.

        :param items: A list of lists where each sublist contains [factor, price].
        :param budget: The total budget available for purchasing items.
        :return: The maximum number of items that can be acquired.
        """
        maxFactor = 1500
        freq = [0] * (maxFactor + 1)
        for factor, price in items:
            freq[factor] += 1

        gain = [0] * (maxFactor + 1)
        for f in range(1, maxFactor + 1):
            if freq[f] > 0:
                totalGain = 0
                for multiple in range(f, maxFactor + 1, f):
                    totalGain += freq[multiple]
                gain[f] = totalGain

        dp = [-1] * (budget + 1)
        dp[0] = 0
        validWeights = [0]

        for factor, price in items:
            if price > budget:
                continue

            gainFirst = gain[factor]
            bought = [-1] * (budget + 1)

            for w in validWeights:
                if w + price <= budget:
                    v = dp[w] + gainFirst
                    if v > bought[w + price]:
                        bought[w + price] = v

            for w in range(price, budget + 1):
                if bought[w - price] != -1:
                    v = bought[w - price] + 1
                    if v > bought[w]:
                        bought[w] = v

            for w in range(budget + 1):
                if bought[w] > dp[w]:
                    dp[w] = bought[w]

            validWeights = [w for w in range(budget + 1) if dp[w] != -1]

        return max(dp)