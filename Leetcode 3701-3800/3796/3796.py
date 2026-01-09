# Leetcode 3796: Find Maximum Value in a Constrained Sequence
# https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/
# Solved on 9th of January, 2026
class Solution:
    def findMaxVal(self, n: int, restrictions: list[list[int]], diff: list[int]) -> int:
        """
        Finds the maximum possible value in a constrained sequence.

        Args:
            n: The length of the sequence.
            restrictions: A list of [index, maxValue] pairs, where maxValue is an upper bound for the element at index.
            diff: A list of differences, where diff[i] represents the maximum allowed difference between sequence[i+1]
                  and sequence[i].

        Returns:
            The maximum possible value in the constrained sequence.
        """

        limitArr = [float('inf')] * n
        limitArr[0] = 0

        for idx, maxVal in restrictions:
            limitArr[idx] = min(limitArr[idx], maxVal)

        for i in range(1, n):
            limitArr[i] = min(limitArr[i], limitArr[i - 1] + diff[i - 1])

        for i in range(n - 2, -1, -1):
            limitArr[i] = min(limitArr[i], limitArr[i + 1] + diff[i])

        return int(max(limitArr))