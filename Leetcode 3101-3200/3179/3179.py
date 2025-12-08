# Leetcode 3179: Find the N-th Value After K Seconds
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/
# Solved on 8th of December, 2025
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        """
        Calculates the n-th value after k seconds.

        Args:
            n (int): The number of elements.
            k (int): The number of seconds.

        Returns:
            int: The n-th value after k seconds, modulo 10^9 + 7.
        """
        modulo = 10**9 + 7
        result = 1
        for i in range(n - 1):
            result *= (k + 1 + i)
            result //= (i + 1)

        return result % modulo