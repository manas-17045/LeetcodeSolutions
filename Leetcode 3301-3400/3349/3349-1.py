# Leetcode 3349: Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
# Solved on 14th of October, 2025
class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        """
        Detects if there exist two adjacent strictly increasing subarrays of length k.
        :param nums: A list of integers.
        :param k: The desired length of the increasing subarrays.
        :return: True if two such adjacent subarrays exist, False otherwise.
        """
        arrayLength = len(nums)

        def isStrctlyIncreasing(startIndex):
            loopEnd = startIndex + k - 1
            for i in range(startIndex, loopEnd):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        possibleStarts = arrayLength - 2 * k + 1
        for i in range(possibleStarts):
            # Check the first subarray starting at index `i`.
            if isStrctlyIncreasing(i):
                # If the first is increasing, check the adjacent subarray starting at i + k`.
                if isStrctlyIncreasing(i + k):
                    return True

        return False