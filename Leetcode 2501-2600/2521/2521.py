# Leetcode 2521: Distinct Prime factors of Product of Array
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/
# Solved on 29th of November, 2025
class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        """
        Calculates the number of distinct prime factors of the product of all numbers in the input list.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The count of distinct prime factors.
        """
        primeFactors = set()
        for number in set(nums):
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    primeFactors.add(divisor)
                    while number % divisor == 0:
                        number //= divisor
                divisor += 1
            if number > 1:
                primeFactors.add(number)

        return len(primeFactors)