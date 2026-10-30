# Leetcode 4063: Longest Subarray Divisible by K with At Most One Negation I
# https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-i/
# Solved on 30th of October, 2026
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        """
        Calculates the length of the longest subarray whose sum is divisible
        by k or can become divisible by k by negating at most one element.

        Parameters:
            nums (list[int]): The array of integers.
            k (int): The divisor used to test divisibility.

        Returns:
            int: The maximum length of a valid subarray, or 0 if none exists.
        """
        totalLength = len(nums)
        doubledRemainders = [(2 * elementVal) % k for elementVal in nums]
        maxLen = 0

        for leftIndex in range(totalLength):
            if totalLength - leftIndex <= maxLen:
                break

            currentSum = 0
            seenRemainders = set()

            for rightIndex in range(leftIndex, totalLength):
                currentSum = (currentSum + nums[rightIndex]) % k
                seenRemainders.add(doubledRemainders[rightIndex])

                if currentSum == 0 or currentSum in seenRemainders:
                    subarrayLength = rightIndex - leftIndex + 1
                    if subarrayLength > maxLen:
                        maxLen = subarrayLength

        return maxLen