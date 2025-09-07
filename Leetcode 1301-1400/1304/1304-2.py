# Leetcode 1304: Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Solved on 7th of September, 2025
class Solution:
    def sumZero(self, n: int) -> list[int]:
        """
        Given an integer n, return any array containing n unique integers such that they add up to 0.

        Args:
            n (int): The number of unique integers to generate.
        Returns:
            list[int]: An array containing n unique integers that sum to 0.
        """
        # If n is odd, include 0 and make (n - 1) // 2 pairs; if even, make n // 2 pairs.
        res: list[int] = []
        if n % 2 == 1:
            res.append(0)

        # Create pairs (i, -i) until we have n numbers
        half = n // 2
        for i in range(1, half + 1):
            res.append(i)
            res.append(-i)

        return res