# Leetcode 3349: Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
# Solved on 14th of October, 2025
class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        """
        Checks if there exist two adjacent strictly increasing subarrays of length k.
        :param nums: A list of integers.
        :param k: The required length of the subarrays.
        :return: True if such subarrays exist, False otherwise.
        """
        n = len(nums)

        # helper function to check if a subarray is strictly increasing
        def is_strictly_increasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        # Check all possible positions for the adjacent subarrays of length k
        for i in range(n - 2 * k + 1):
            # Check if subarray starting at i is strictly increasing
            if is_strictly_increasing(i):
                # Check if adjacent subarray starting at i + k is also strictly increasing
                if is_strictly_increasing(i + k):
                    return True

        return False