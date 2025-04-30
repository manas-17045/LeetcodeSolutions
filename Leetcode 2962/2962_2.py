# Leetcode 2962: Count Subarrays Where Max Element Appears at Least K Times
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# Date: 29th of April, 2025

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays where the maximum element occurs at least `k` times
        consecutively. The method finds the positions of the maximum element in the given
        array and calculates the possible subarrays for each starting position of `k`
        consecutive occurrences of the maximum element.

        The algorithm computes the number of ways you can choose the beginning and
        the end of a subarray such that the subarray contains `k` consecutive occurrences
        of the maximum element. These counts are then multiplied and accumulated to
        obtain the final result.

        :param nums: A list of integers representing the array to analyze.
        :type nums: list[int]
        :param k: An integer representing the number of consecutive occurrences
            of the maximum element required.
        :type k: int
        :return: The number of subarrays where the maximum element appears
            consecutively at least `k` times.
        :rtype: int
        """
        max_element = max(nums)
        n = len(nums)
        count = 0

        # Get positions of the maximum element
        max_positions = [i for i in range(n) if nums[i] == max_element]

        # If there are fewer than k occurrences of the maximum element, return 0
        if len(max_positions) < k:
            return 0

        # For each possible starting position of k consecutive occurrences of max_element
        for i in range(len(max_positions) - k + 1):
            # For each subarray to be valid:
            # 1. It must start at or before max_positions[i]
            # 2. It must end at or after max_positions[i + k - 1]

            # Calculate the left bound (how many ways to choose the start)
            left_bound = max_positions[i] + 1
            if i > 0:
                # We can start anywhere after the previous max position
                left_bound = max_positions[i] - max_positions[i - 1]

            # Calculate the right bound (how many ways to choose the end)
            right_bound = n - max_positions[i + k - 1]

            # The number of valid subarrays is the product of these two bounds
            count += left_bound * right_bound

        return count