# Leetcode 2972: Count the Number of Incremovable Subarrays II
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/
# Solved on 18th of October, 2025
class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        """
        Calculates the number of incremovable subarrays.
        An incremovable subarray is a subarray such that if it is removed,
        the remaining elements form a strictly increasing sequence.

        Args:
            nums: A list of integers.
        Returns:
            The total count of incremovable subarrays.
        """
        n = len(nums)
        # Longest strictly increasing prefix and index p
        p = 0
        while p + 1 < n and nums[p] < nums[p + 1]:
            p += 1

        # Entire array strictly increasing -> every non-empty subarray works
        if p == n - 1:
            return n * (n + 1) // 2

        # Longest strictly increasing suffix start index s
        s = n - 1
        while s - 1 >= 0 and nums[s - 1] < nums[s]:
            s -= 1

        count = 0
        j = s

        # Iterate over possible end index i of the left piece
        for i in range(-1, p + 1):
            # Ensure j is at least s and also at least i + 2
            j = max(j, s, i + 2)

            # If left is non-empty, we need nums[i] < nums[j]
            if i >= 0:
                while j < n and nums[i] >= nums[j]:
                    j += 1

            # Every j in [j...n] gives a valid removal
            if j <= n:
                count += n - j + 1

        return count