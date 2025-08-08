# Leetcode 2369: Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
# Solved on 8th of August, 2025
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        """
        Determines if an array can be partitioned into valid subarrays.
        A valid subarray is either two equal elements, three equal elements, or three consecutive increasing elements.
        :param nums: The input list of integers.
        :return: True if the array can be partitioned into valid subarrays, False otherwise.
        """
        n = len(nums)
        if n < 2:
            return False

        dp_prev3 = False
        dp_prev2 = True
        dp_prev1 = False

        for i in range(2, n + 1):
            curr = False

            # Check partition of last 2 equal elements: [i - 2, i - 1]
            if nums[i - 2] == nums[i - 1] and dp_prev2:
                curr = True

            # If we have at least 3 elements, check 3-equal or 3-consecutive
            if not curr and i >= 3:
                # Three equal elements
                if nums[i - 3] == nums[i - 2] == nums[i - 1] and dp_prev3:
                    curr = True
                # Three consecutive increasing elements
                if not curr and nums[i - 3] + 1 == nums[i - 2] and nums[i - 2] + 1 == nums[i - 1] and dp_prev3:
                    curr = True

            # Shift dp states forward for next iteration
            dp_prev3, dp_prev2, dp_prev1 = dp_prev2, dp_prev1, curr

        # dp_prev1 holds dp[n]
        return dp_prev1