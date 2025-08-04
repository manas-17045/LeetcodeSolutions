# Leetcode 1049: Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/
# Solved on 4th of August, 2025
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Calculates the minimum possible weight of the last stone remaining after crushing operations.
        This problem is equivalent to partitioning the stones into two groups such that the
        absolute difference of their sums is minimized.

        :param stones: A list of integers representing the weights of the stones.
        :return: The minimum possible weight of the last stone.
        """
        total = sum(stones)
        # dp as a bitmask: bit i is 1 if sum i is achievable
        dp = 1  # Only sum 0 is achievable initially

        # For each stone weight w, shift the mask by w and OR it in.
        for w in stones:
            dp |= dp << w

        half = total // 2
        # Find the largest achievable subset-sum <= total//2
        for s in range(half, -1, -1):
            if (dp >> s) & 1:
                # Best split gives difference total - 2 * s
                return total - 2 * s
        # Fallback, though loop always returns
        return 0