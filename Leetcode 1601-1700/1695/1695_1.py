# Leetcode 1695: Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/
# Solved on 22nd of July, 2025
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a unique subarray.

        :param nums: A list of integers.
        :return: The maximum sum of a subarray with unique elements.
        """
        left = 0
        maxScore = 0
        currentScore = 0
        seenNumbers = set()

        for right in range(len(nums)):
            while nums[right] in seenNumbers:
                currentScore -= nums[left]
                seenNumbers.remove(nums[left])
                left += 1

            currentScore += nums[right]
            seenNumbers.add(nums[right])
            maxScore = max(maxScore, currentScore)

        return maxScore