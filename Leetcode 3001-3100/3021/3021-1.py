# Leetcode 3021: Alice and Bob Playing Flower Game
# https://leetcode.com/problems/alice-and-bob-playing-flower-game/
# Solved on 29th of August, 2025
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Calculates the number of ways Alice and Bob can pick flowers such that the sum of their chosen flowers is odd.

        Args:
            n (int): The maximum number of flowers Alice can pick.
            m (int): The maximum number of flowers Bob can pick.

        Returns:
            int: The number of pairs (x, y) such that 1 <= x <= n, 1 <= y <= m, and x + y is odd.
        """
        oddN = (n + 1) // 2
        evenN = n // 2
        oddM = (m + 1) // 2
        evenM = m // 2

        return oddN * evenM + evenN * oddM