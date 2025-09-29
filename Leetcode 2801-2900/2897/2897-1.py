# Leetcode 2897: Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
# Solved on 29th of September, 2025
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        """
        Applies operations on an array to maximize the sum of squares.

        Args:
            nums: A list of integers.
            k: An integer representing the number of elements to consider for the sum of squares.
        Returns:
            The maximum sum of squares modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        bitCounts = [0] * 31
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bitCounts[i] += 1

        newNums = [0] * k
        for j in range(31):
            count = min(k, bitCounts[j])
            for i in range(count):
                newNums[i] += (1 << j)

        totalSumOfSquares = 0
        for num in newNums:
            totalSumOfSquares = (totalSumOfSquares + pow(num, 2, mod)) % mod

        return totalSumOfSquares