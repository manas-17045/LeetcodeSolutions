# Leetcode 3397: Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
# Solved on 9th of October, 2025
class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum number of distinct elements possible in the array after applying operations.
        In each operation, an element `num` can be changed to any integer in the range `[num - k, num + k]`.

        Args:
            nums: A list of integers.
            k: An integer representing the maximum allowed change for each element.

        Returns:
            The maximum number of distinct elements.
        """
        nums.sort()

        distinctCount = 0
        lastValue = float('-inf')

        for num in nums:
            startRange = num - k
            endRange = num + k

            potentialValue = max(startRange, lastValue + 1)

            if potentialValue <= endRange:
                distinctCount += 1
                lastValue = potentialValue

        return distinctCount