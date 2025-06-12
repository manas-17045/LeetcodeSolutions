# Leetcode 2412: Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions/
# Solved on 12th of June, 2025

class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        """
        Calculates the minimum initial money required to complete all transactions.

        Args:
            transactions: A list of transactions, where each transaction is a list
                          [cost, cashback].

        Returns:
            The minimum initial money needed.

        The logic is to separate transactions into those with net gain (cashback >= cost)
        and those with net loss (cashback < cost). We need enough money to cover the
        total loss from all loss transactions, plus the maximum single requirement
        from either the highest cost in the gain group or the highest cashback in the loss group.
        """
        total_loss = 0
        max_cost_gain = 0
        max_cashback_loss = 0

        for cost, cash in transactions:
            if cash >= cost:
                # Net >= 0: track the maximum cost in gain group
                if cost > max_cost_gain:
                    max_cost_gain = cost
            else:
                # Net < 0: Accumulate loss, track max cashback in loss group
                total_loss += (cost - cash)
                if cash > max_cashback_loss:
                    max_cashback_loss = cash

        # We need enough to cover all losses plus the worst single requirement.
        result = total_loss + max(max_cost_gain, max_cashback_loss)

        return result