# Leetcode 2483: Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/
# Solved on 19th of November, 2025
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Calculates the best closing time for a shop to minimize penalty.

        Args:
            customers (str): A string representing customer visits for each hour. 'Y' means a customer visited, 'N' means no customer.
        Returns:
            int: The best closing hour (0-indexed) that minimizes the penalty.
        """
        maxScore = 0
        currentScore = 0
        bestHour = 0

        for i, customer in enumerate(customers):
            if customer == 'Y':
                currentScore += 1
            else:
                currentScore -= 1

            if currentScore > maxScore:
                maxScore = currentScore
                bestHour = i + 1

        return bestHour