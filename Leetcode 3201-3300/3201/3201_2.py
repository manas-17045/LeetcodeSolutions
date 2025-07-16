# Leetcode 3201: Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
# Solved on 16th of July, 2025
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        """
        Calculates the maximum length of a subsequence of `nums` such that the sum of any two adjacent elements in the subsequence is even,
        or the sum of any two adjacent elements in the subsequence is odd.

        Args:
            nums: A list of integers.
        Returns:
            The maximum possible length of such a subsequence.
        """
        # Count total evens and odds
        evens = sum(1 for x in nums if x % 2 == 0)
        odds = len(nums) - evens

        # Pick all evens or all odds -> adjacent sums are even
        best = max(evens, odds)

        # Pick an alternating parity subsequence -> adjacent sums are odd
        def greedy_alternate(start_parity: int) -> int:
            cnt = 0
            need = start_parity
            for x in nums:
                if x % 2 == need:
                    cnt += 1
                    need ^= 1
            return cnt

        best = max(best, greedy_alternate(0), greedy_alternate(1))
        return best