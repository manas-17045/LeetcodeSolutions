# Leetcode 1304: Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Solved on 7th of September, 2025
class Solution:
    def sumZero(self, n: int) -> list[int]:
        """
        Given an integer n, return any array containing n unique integers such that they add up to 0.

        :param n: The number of unique integers to generate.
        :return: A list of n unique integers that sum up to zero.
        """
        resultArray = []

        # Add pairs of (i, -i) to the array.
        for i in range(1, n // 2 + 1):
            resultArray.append(i)
            resultArray.append(-i)

        # If n is odd, the array is currently one element short.
        # Add a 0 to complete the array and keep the sum at zero.
        if n % 2 != 0:
            resultArray.append(0)

        return resultArray