# Leetcode 3779: Minimum Number of Operations to Have Distinct Elements
# https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/
# Solved on 25th of December, 2025
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make all elements in the array distinct.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations required.
        """
        seenElements = set()
        distinctSuffixStart = 0
        arrayLength = len(nums)

        for i in range(arrayLength - 1, -1, -1):
            if nums[i] in seenElements:
                distinctSuffixStart = i + 1
                break

            seenElements.add(nums[i])

        return (distinctSuffixStart + 2) // 3