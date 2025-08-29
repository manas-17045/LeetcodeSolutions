# Leetcode 3021: Alice and Bob Playing Flower Game
# https://leetcode.com/problems/alice-and-bob-playing-flower-game/
# Solved on 29th of August, 2025
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Calculates the number of pairs (x, y) such that 1 <= x <= n, 1 <= y <= m, and x + y is odd.

        Args:
            n (int): The upper bound for x.
            m (int): The upper bound for y.
        Returns:
            int: The number of pairs (x, y) where x + y is odd.
        """
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2

        return (odd_n * even_m) + (even_n * odd_m)