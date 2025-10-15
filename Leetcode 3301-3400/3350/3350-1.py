# Leetcode 3350: Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/
# Solved on 15th of October, 2025
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible value of k such that there exist two adjacent increasing subarrays,
        each of length at least k.

        Args:
            nums: A list of integers.
        Returns:
            The maximum integer k satisfying the condition.
        """
        listSize = len(nums)

        maxK = 0
        previousLength = 0
        currentLength = 1

        for i in range(1, listSize):
            if nums[i] > nums[i - 1]:
                currentLength += 1
            else:
                maxK = max(maxK, currentLength // 2)

                maxK = max(maxK, min(previousLength, currentLength))

                previousLength = currentLength
                currentLength = 1

        # Perform a final update for the last subarray in the list
        maxK = max(maxK, currentLength // 2)
        maxK = max(maxK, min(previousLength, currentLength))

        return maxK