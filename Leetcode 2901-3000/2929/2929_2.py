# Leetcode 2929: Distribute Candies among Children II
# https://leetcode.com/problems/distribute-candies-among-children-ii/
# Solved on 1st of June, 2025

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Calculates the number of ways to distribute n candies among 3 children
        such that each child receives at most limit candies.

        Args:
            n: The total number of candies.
            limit: The maximum number of candies each child can receive.

        Returns:
            The number of ways to distribute the candies.
        """
        d = limit + 1

        def f(k: int) -> int:
            if k < 0:
                return 0
            return (k + 2) * (k + 1) // 2

        return (
            f(n)
            - 3 * f(n - d)
            + 3 * f(n - 2 * d)
            - f(n - 3 * d)
        )