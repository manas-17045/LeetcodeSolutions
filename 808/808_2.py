# Leetcode 808: Soup Servings
# https://leetcode.com/problems/soup-servings/
# Solved on 8th of August, 2025
import math
from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        """
        Calculates the probability that soup A is served first, given initial amounts of soup A and B.

        Args:
            n (int): The initial amount of soup A and soup B in milliliters.

        Returns:
            float: The probability that soup A is served first.
        """

        # For extremely large n the result is effectively 1
        if n > 4800:
            return 1.0

        # Scale down by 25 (operations are multiples of 25)
        N = math.ceil(n / 25)

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            # Four equally likely serving operations (in units of 25)
            return 0.25 * (
                    dp(a - 4, b)  # 100 A, 0 B -> 4,0
                    + dp(a - 3, b - 1)  # 75 A, 25 B -> 3,1
                    + dp(a - 2, b - 2)  # 50 A, 50 B -> 2,2
                    + dp(a - 1, b - 3)  # 25 A, 75 B -> 1,3
            )

        return dp(N, N)