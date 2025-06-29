# Leetcode 1498: Number of Subsequences That Satisfy the Given Sum Condition
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# Solved on 29th of June, 2025
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Calculates the number of non-empty subsequences of `nums` such that the sum
        of the minimum and maximum elements in the subsequence is less than or equal to `target`.

        Args:
            nums: A list of integers.
            target: An integer target value.

        Returns:
            The number of such subsequences modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        # Precompute powers of 2 up to n, modulo MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0
        left, right = 0, (n - 1)

        while left <= right:
            # If the smallest + largest in [left..right] is <= target,
            # then for this left, any subset of the (right-left) elements
            # to its right yields a valid subsequence.
            if nums[left] + nums[right] <= target:
                ans = (ans + pow2[right - left]) % MOD
                left += 1
            else:
                # Too big, we need to try a smaller one
                right -= 1

        return ans