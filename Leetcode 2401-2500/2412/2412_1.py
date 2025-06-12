# Leetcode 2412: Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions/
# Solved on 12th of June, 2025

class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        """
        Calculates the minimum money required before starting all transactions.

        To complete all transactions, we need enough money to cover the maximum
        temporary deficit incurred during the process. This deficit occurs when
        we perform a transaction where the cost is greater than the cashback.
        The total minimum money required is the sum of all net losses from
        lossy transactions plus the maximum of either the highest cost among
        gainful transactions or the highest cashback among lossy transactions.

        Args:
            transactions: A list of transactions, where each transaction is [cost, cashback].

        Returns: The minimum money required.
        """
        totalNetLoss = 0
        maxCostAmongGainful = 0
        maxCashbackAmongLossy = 0

        for cost, cashback in transactions:
            if cost > cashback:
                totalNetLoss += cost - cashback
                if cashback > maxCashbackAmongLossy:
                    maxCashbackAmongLossy = cashback
            else:
                if cost > maxCostAmongGainful:
                    maxCostAmongGainful = cost

        result = totalNetLoss + max(maxCostAmongGainful, maxCashbackAmongLossy)

        return result