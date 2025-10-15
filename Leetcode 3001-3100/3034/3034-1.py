# Leetcode 3034: Number of Subarrays That Match a Pattern I
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/
# Solved on 15th of October, 2025
class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        """
        Counts the number of subarrays in `nums` that match the given `pattern`.

        Args:
            nums: A list of integers representing the main array.
            pattern: A list of integers representing the pattern to match.
                     1 for increasing, -1 for decreasing, 0 for equal.
        Returns:
            The number of subarrays in `nums` that match the `pattern`.
        """

        n = len(nums)
        m = len(pattern)

        diffs = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diffs.append(1)
            elif nums[i + 1] < nums[i]:
                diffs.append(-1)
            else:
                diffs.append(0)

        matchCount = 0
        diffsLength = n - 1

        for i in range(diffsLength - m + 1):
            if diffs[i:i + m] == pattern:
                matchCount += 1

        return matchCount