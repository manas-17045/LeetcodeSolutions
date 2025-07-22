# Leetcode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Solved on 22nd of July, 2025
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        """
        Calculates the number of subarrays of size k with an average greater than or equal to the threshold.

        Args:
            arr (list[int]): The input array of integers.
            k (int): The size of the subarray.
            threshold (int): The minimum average required for a subarray.
        Returns:
            int: The number of subarrays that meet the criteria.
        """
        # target sum for a window of size k to have average >= threshold
        target = k * threshold

        # Sum of the first window
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0

        # Slide the window over the rest of the array
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target:
                count += 1

        return count