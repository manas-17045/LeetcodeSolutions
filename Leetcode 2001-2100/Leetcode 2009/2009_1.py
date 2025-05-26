# Leetcode 2009: Minimum Number of Operations to Make Array Continuous
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
# Solved on 17th of May, 2025

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations needed to make an array continuous.

        An array is considered continuous if it contains n distinct integers and, after sorting,
        the difference between the maximum and minimum elements is n - 1.

        Args:
            nums: A list of integers.

        Returns:
            The minimum number of operations required to make the array continuous.

        Example:
            minOperations([4,2,5,3]) == 0  (already continuous)
        """
        n = len(nums)

        # Step 1: Get unique elements and sort them.
        # These are the distinct values from the input array that we could potentially keep.
        unique_nums = sorted(list(set(nums)))
        m = len(unique_nums)    # Number of unique elements

        # Tracks the maximum number of elements we can keep
        max_elements_kept = 0

        # Step 2: Sliding window approach
        # right_ptr indicates the (exclusive) and of the current window of unique_nums.
        right_ptr = 0

        # left_ptr indicates the (inclusive) start of the current window of unique_nums.
        for left_ptr in range(m):
            # unique_nums[left_ptr] is the smallest element in the current selection
            # To form a continuous array pf length n including unique_nums[left_ptr],
            # all selected elements must be <= unique_nums[left_ptr] + n - 1.
            # Let this upper bound be target_max_val_for_window.
            target_max_val_for_window = unique_nums[left_ptr] + n - 1

            # Expand the window by moving right_ptr:
            # Include all elements from unique)nums that are within the range
            # [unique_nums[left_ptr], target_max_val_for_window].
            while right_ptr < m and unique_nums[right_ptr] <= target_max_val_for_window:
                right_ptr += 1

            # The elements unique_nums[left_ptr ... right_ptr - 1] are those selected.
            # The count is (right_ptr - left_ptr).
            num_elements_in_current_selection = right_ptr - left_ptr
            max_elements_kept = max(max_elements_kept, num_elements_in_current_selection)

        # Step 3: Calculate minimum operations.
        # We need n elements in the final continuous array.
        # If we keep max_elements_kept, we need to change n - max_elements_kept elements.
        return n - max_elements_kept