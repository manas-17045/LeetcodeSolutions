# Leetcode 3356: Zero Array Transformation II
# https://leetcode.com/problems/zero-array-transformation-ii/
# Solved on 25th of May, 2025

class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Finds the minimum number of initial queries needed to make all elements in the array `nums` zero.

        Each query `[l, r, val]` allows decrementing any element `nums[i]` where `l <= i <= r` by at most `val`.
        We can apply any number of allowed decrements from the first `k` queries to each element.
        The goal is to find the smallest `k` such that it's possible to make all elements in `nums` zero.

        Args:
            nums: A list of non-negative integers.
            queries: A list of queries, where each query is `[l, r, val]`.

        Returns:
            The minimum number of initial queries required.
        """
        n = len(nums)
        m = len(queries)

        # Helper function to check if nums can be made zero with the first k_val queries
        def can_make_zero(k_val: int) -> bool:
            # If k_val is 0, no queries are applied.
            # The array can be made zero if and only if all its elements are already zero.
            # This case is naturally handled by the general logic below:
            # diff_array would remain all zeros, current_total_decrement would be 0 for all elements.
            # Then, it checks if 0 < nums[i] for any element.

            # Initialize difference array. It stores the net change at each point.
            # Size n+1: indices 0 to n. diff_array[n] is used when a query range ends at n-1.
            diff_array = [0] * (n + 1)

            # Apply the first k_val queries to populate the difference array.
            # Each query [l, r, val] means elements from index l to r can be decremented by val.
            # This translates to: add val at index l, subtract val at index r+1 in the difference array.
            for i in range(k_val):
                l_j, r_j, val_j = queries[i]
                diff_array[l_j] += val_j

                # Constraints: 0 <= l_j <= r_j < n (nums.length).
                # So, r_j can be at most n-1.
                # Thus, r_j + 1 can be at most n.
                # diff_array[r_j + 1] is always a valid index (it can be from diff_array[1] to diff_array[n]).
                diff_array[r_j + 1] -= val_j

            # Reconstruct the total possible decrement for each element nums[i]
            # by taking prefix sums of the diff_array.
            # Check if this total possible decrement is sufficient for each nums[i].
            current_total_decrement = 0
            for i in range(n):  # Iterate through indices of the nums array (0 to (n - 1))
                current_total_decrement += diff_array[i]
                if current_total_decrement < nums[i]:
                    # The maximum possible decrement for nums[i] using the first k_val queries
                    # is less than the value of nums[i] itself.
                    # So, nums[i] cannot be reduced to 0.
                    # (Constraint from problem: 0 <= nums[i] <= 10^9, so nums[i] is non-negative)
                    return False

            # If all elements can be reduced to zero (or made negative, which means they passed 0)
            return True

        # Binary search for the minimum k (number of queries).
        # k can range from 0 (no queries used) to m (all queries used).
        low = 0
        high = m
        min_k_found = -1    # Initialize to -1, signifies that no suitable k has been found yet.

        while low <= high:
            # mid represents the number of queries to consider (from the start of queries list)
            mid = low + (high - low) // 2

            if can_make_zero(mid):
                # If nums can be made zero using 'mid' queries:
                min_k_found = mid  # 'mid' is a potential answer. Store it.
                high = mid - 1  # Try to find an even smaller k (more optimal solution).
            else:
                # If nums cannot be made zero using 'mid' queries:
                low = mid + 1  # 'mid' is too small, need to use more queries (larger k).

        return min_k_found