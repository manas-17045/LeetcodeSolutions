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
            target: An integer representing the maximum allowed sum of min and max elements.

        Returns:
            The number of such subsequences, modulo 10^9 + 7.
        """
        n = len(nums)
        mod = 10**9 + 7

        nums.sort()

        powersOfTwo = [1] * n
        for i in range(1, n):
            powersOfTwo[i] = (powersOfTwo[i - 1] * 2) % mod

        answer = 0
        left = 0
        right = n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                answer = (answer + powersOfTwo[right - left]) % mod
                left += 1
            else:
                right -= 1

        return answer