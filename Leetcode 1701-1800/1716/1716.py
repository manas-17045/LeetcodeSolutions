# Leetcode 1716: Calculate Money in Leetcode Bank
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Solved on 25th of October, 2025
class Solution:
    def totalMoney(self, n: int) -> int:
        """
        Calculates the total amount of money in the Leetcode bank after n days.

        Args:
            n: The number of days.
        Returns:
            The total amount of money Leetcode will have.
        """

        numFullWeeks = n // 7
        remainingDays = n % 7

        totalFromWeeks = (
                (7 * numFullWeeks * (numFullWeeks + 1) // 2) +
                (21 * numFullWeeks)
        )

        startMoney = numFullWeeks = 1

        totalFromDays = (
                (remainingDays * (2 * startMoney + remainingDays - 1)) // 2
        )

        totalMoney = totalFromWeeks + totalFromDays

        return totalMoney