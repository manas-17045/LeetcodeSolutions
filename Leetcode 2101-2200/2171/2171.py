# Leetcode 2171: Removing Minimum Number of Magic Beans
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
# Solved on 6th of December, 2025
class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        """
        Calculates the minimum number of magic beans to remove such that all remaining bags have the same number of beans.

        Args:
            beans: A list of integers representing the number of beans in each bag.

        Returns:
            An integer representing the minimum number of beans to remove.
        """
        beans.sort()

        totalSum = sum(beans)
        n = len(beans)
        maxRemaining = 0
        for i in range(n):
            remaining = beans[i] * (n - i)

            if remaining > maxRemaining:
                maxRemaining = remaining

        return totalSum - maxRemaining