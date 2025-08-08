# Leetcode 1331: Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/
# Solved on 8th of August, 2025
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        Transforms an array of integers into an array where each element is replaced by its rank.
        The rank is an integer starting from 1. If two numbers are equal, their ranks must be the same.
        Smaller numbers have smaller ranks.
        :param arr: A list of integers.
        :return: A list of integers where each element is replaced by its rank.
        """
        if not arr:
            return []
        # Create sorted list of unique values and map each to its rank
        unique_sorted = sorted(set(arr))
        rank_map = {val: i + 1 for i, val in enumerate(unique_sorted)}
        # Replace each original value with its rank.
        return [rank_map[val] for val in arr]