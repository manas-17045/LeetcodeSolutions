# Leetcode 3381: Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
# Solved on 3rd of August, 2025
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum sum of a subarray whose length is a multiple of k.

        Args:
            nums: A list of integers.
            k: An integer representing the multiple for subarray length.
        Returns:
            The maximum sum of a subarray whose length is a multiple of k.
        """
        # Prefix sum
        pref = 0
        # For each residue 0 <= r < k, store the minimum we've seen ar an index i with i % k == r
        # Start with only residue 0 seen at i = 0, pref = 0
        min_pref = [None] * k
        min_pref[0] = 0

        best = -10**30  # sufficiently small initial value

        for i, x in enumerate(nums, 1):
            pref += x
            r = i % k

            # If we've seen this residue before, we can form a length-multiple-of-k subarray
            if min_pref[r] is not None:
                best = max(best, pref - min_pref[r])

            # Update the minimum prefix sum for this residue
            if min_pref[r] is None or pref < min_pref[r]:
                min_pref[r] = pref

        return best