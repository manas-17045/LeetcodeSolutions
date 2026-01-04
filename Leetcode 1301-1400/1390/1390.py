# Leetcode 1390: Four Divisors
# https://leetcode.com/problems/four-divisors/
# Solved on 4th of January, 2026
import math


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        """
        Calculates the sum of divisors for numbers in the input list that have exactly four divisors.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The total sum of divisors for numbers with exactly four divisors.
        """
        totalSum = 0
        for num in nums:
            divisors = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                    if len(divisors) > 4:
                        break

            if len(divisors) == 4:
                totalSum += sum(divisors)

        return totalSum