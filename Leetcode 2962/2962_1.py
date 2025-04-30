# Leetcode 2962: Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# Date: 29th of April, 2025

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays where the maximum value of each subarray appears
        fewer than a specified number of times (k). It operates using a sliding window approach
        to maintain an efficient count of valid subarrays.

        The function processes the input list to identify subarrays that satisfy the given condition.
        To determine the counts, it uses a sliding window technique, expanding and shrinking the
        window dynamically based on the occurrences of the maximum value in the subarray.

        :param nums:
            The list of integers representing the array for which subarrays are counted.
        :param k:
            The integer specifying the condition that the maximum value in the subarray
            must occur fewer than `k` times.
        :return:
            An integer representing the total count of subarrays, meeting the specified
            condition within the given list of integers.
        """
        n = len(nums)

        # Basic edge cases
        if n == 0 or k <= 0:
            return 0

        # Find the maximum element in the array
        max_val = -1
        try:
            max_val = max(nums)
        except ValueError:
            # Handles empty list, though constraints say n >= 1.
            return 0

        count = 0

        # Left pointer of the sliding window
        l = 0

        # Count of max_val on the current_window [l...r]
        max_count_in_window = 0

        # Iterate with the sliding window
        for r in range(n):
            # Expand window to the right
            if nums[r] == max_val:
                max_count_in_window += 1

            # Shrink window from the left of the count condition is met or exceeded
            # We keep shrinking as long as the window [l...r] has k or more max_val
            while max_count_in_window >= k:
                # Check the element at the left pointer before shrinking
                if nums[l] == max_val:
                    max_count_in_window -= 1
                # Shrink the window
                l += 1

            # After the while loop, the window [l...r] has < k max_val.
            # The crucial point is that any subarray starting at an index l
            # where 0 <= l' < l, when ending at r, `must` have contained
            # at least k occurrences of max_val (because l only moved
            # forward when the count was >= k).
            # The number of such valid starting indices l' is exactly `l`.
            count += l

        return count