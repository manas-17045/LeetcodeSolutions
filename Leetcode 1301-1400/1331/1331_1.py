# Leetcode 1331: Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/
# Solved on 8th of August, 2025
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        """
        Transforms an array by replacing each element with its rank.

        Args:
            arr: A list of integers.
        Returns:
            A list of integers where each element is replaced by its rank.
        """
        sortedUniqueNumbers = sorted(list(set(arr)))

        rankMapping = {}
        for index, number in enumerate(sortedUniqueNumbers):
            rankMapping[number] = index + 1

        resultArray = [rankMapping[number] for number in arr]

        return resultArray