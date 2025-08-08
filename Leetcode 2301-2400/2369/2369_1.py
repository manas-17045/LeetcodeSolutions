# Leetcode 2369: Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
# Solved on 8th of August, 2025
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        """
        Checks if the given array `nums` can be partitioned into valid subarrays.
        A valid subarray is either:
        1. Two consecutive elements with equal values.
        2. Three consecutive elements with equal values.
        3. Three consecutive elements with consecutive increasing values (e.g., 1, 2, 3).
        :param nums: The input list of integers.
        :return: True if the array can be partitioned into valid subarrays, False otherwise.
        """
        n = len(nums)

        threeBack = True
        twoBack = False
        oneBack = (nums[0] == nums[1])

        # Iterate from the third element to the end
        for i in range(3, n + 1):
            currentDp = False

            # Check for a valid 2-element partition ending at i
            # This requires the prefix of length i-2 to be valid.
            if nums[i - 2] == nums[i - 1] and twoBack:
                currentDp = True

            # Check for a valid 3-element partition ending at i
            # This requires the prefix of length i-3 to be valid.
            if (nums[i - 3] == nums[i - 2] == nums[i - 1] or (nums[i - 3] + 1 == nums[i - 2] and nums[i - 2] + 1 == nums[i - 1])) and threeBack:
                currentDp = True

            # Shift the dp states for the next iteration
            threeBack = twoBack
            twoBack = oneBack
            oneBack = currentDp

        return oneBack