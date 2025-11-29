# Leetcode 2507: Smallest Value After Replacing With Sum of Prime Factors
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
# Solved on 29th of November, 2025
class Solution:
    def smallestValue(self, n: int) -> int:
        """
        Calculates the smallest value obtained by repeatedly replacing a number with the sum of its prime factors.

        Args:
            n: The initial integer.
        Returns:
            The smallest value reached after the replacement process stabilizes.
        """
        while True:
            currentSum = 0
            temp = n
            divisor = 2
            while divisor * divisor <= temp:
                while temp % divisor == 0:
                    currentSum += divisor
                    temp //= divisor
                divisor += 1
            if temp > 1:
                currentSum += temp
            if currentSum == n:
                return n
            n = currentSum