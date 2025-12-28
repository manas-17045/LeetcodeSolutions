# Leetcode 3653: XOR After Range Multiplication Queries I
# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
# Solved on 28th of December, 2025
class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Applies a series of multiplication queries to a list of numbers and then calculates the XOR sum of the modified numbers.

        Args:
            nums (list[int]): The initial list of integers.
            queries (list[list[int]]): A list of queries, where each query is [start, end, step, val].

        Returns:
            int: The XOR sum of the numbers after all queries have been applied.
        """
        modVal = 10 ** 9 + 7
        for start, end, step, val in queries:
            for index in range(start, end + 1, step):
                nums[index] = (nums[index] * val) % modVal

        xorResult = 0
        for num in nums:
            xorResult ^= num

        return xorResult