# Leetcode 2537: Count the Number of Good Subarrays
# https://leetcode.com/problems/count-the-number-of-good-subarrays/
from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        """
        Counts the number of "good" subarrays within the given list `nums`, where a "good"
        subarray is defined as a subarray that contains at least `k` pairs of indices `(i, j)`
        such that `nums[i] == nums[j]`.

        The function utilizes a sliding window approach to efficiently calculate the count
        of all good subarrays. It maintains a dynamic range `[left, right]` and keeps track
        of the current frequency of elements within the window and the number of pairs
        formed with the same elements.

        The result is obtained by iteratively expanding the right boundary of the window
        and conditionally shrinking the left boundary to find all starting indices of
        valid subarrays.

        :param nums: List of integers representing the input array.
        :type nums: list[int]
        :param k: Integer threshold representing the minimum number of pairs required
            to consider a subarray as "good".
        :type k: int
        :return: The total number of "good" subarrays in the input list `nums`.
        :rtype: int
        """
        n = len(nums)
        left = 0    # Left boundary of the sliding window
        total_good_subarrays = 0    # Accumulator for the result
        current_pairs = 0   # Number of pairs in the current window [left, right]

        # Frequency map for elements within the current window [left, right]
        freq = defaultdict(int)

        # Iterate through the array with the right boundary of the window
        for right in range(n):
            # Current element being added to the window
            val = nums[right]

            # --- Expand window by adding nums[right]
            # Adding 'val' creates new pairs with existing identical elements
            # The number of new pairs formed is equal to the frequency of 'val' before adding it.
            current_pairs += freq[val]

            # Increment the frequency count for the added element
            freq[val] += 1

            # --- Shrink window from the left ---
            # While the current window [left, right] has at least k pairs,
            # it means this window (and potentially) larger ones ending at 'right')
            # contributes to the count. We shrink the window from the left
            # until it no longer satisfies the condition.
            while current_pairs >= k:
                # Element to be removed from the left
                removed_val = nums[left]

                # Decrement frequency first 'before' calculating pairs lost.
                freq[removed_val] -= 1

                # Removing 'removed_val' breaks the pairs it formed with the other instances of 'removed_val'
                # remaining in the window [left + 1, right]
                # The number of pairs lost is equal to the remaining
                # frequency count of 'removed_val'.
                current_pairs -= freq[removed_val]

                # Move the left boundary one step to the right
                left += 1

            # --- Count Contribution ---
            # After the while loop, `left` is the smallest index such that the subarray
            # `nums[left...right]` has 'fewer' than `k` pairs.
            # This implies that any subarray starting at an index `i` where `0 <= i < left`
            # and ending at the current `right` 'will' have at least `k` pairs.
            # The number of such starting indices is `left` (indices 0, 1, ..., left - 1).
            # Therefore, `left` good subarrays end at the current index `right`.
            total_good_subarrays += left

        return total_good_subarrays