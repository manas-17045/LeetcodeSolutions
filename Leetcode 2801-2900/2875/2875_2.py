# Leetcode 2875: Minimum Size Subarray in Infinite Array
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/
# Solved on 20th of August, 2025
class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        """
        Finds the minimum length of a subarray (possibly formed by concatenating `nums` multiple times)
        whose sum is equal to `target`.

        Args:
            nums (list[int]): The input array of integers.
            target (int): The target sum.
        Returns:
            int: The minimum length of such a subarray, or -1 if no such subarray exists.
        """
        total = sum(nums)
        n = len(nums)

        # Number of full repeats we can take
        full_repeats = target // total
        residual = target % total

        # If residual == 0 we can use exactly full_repeats * n elements
        if residual == 0:
            return full_repeats * n

        # Find shortest subarray (within at most two copies) whose sum == residual
        # Use prefix sums and a hashmap of earliest index for each prefix value.
        prefix_to_idx = {0: -1}
        prefix = 0
        best_len = n  # Initialize with sentinel > possible subarray length (we'll compare)

        # Iterate over 2*n elements (simulate two concatenated copies)
        for i in range(2 * n):
            prefix += nums[i % n]
            need = prefix - residual
            if need in prefix_to_idx:
                length = i - prefix_to_idx[need]
                if length < best_len:
                    best_len = length
            # Store the earliest index for this prefix (we want earliest to minimize length)
            # only store if not present because we want earliest occurrence
            if prefix not in prefix_to_idx:
                prefix_to_idx[prefix] = i

        if best_len == n:
            return -1

        return full_repeats * n + best_len