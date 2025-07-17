# Leetcode 3202: Find the Maximum Length of Valid Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/
# Solved on 17th of July, 2025
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum length of a valid subsequence.

        A subsequence is valid if for any two adjacent elements x and y in the subsequence,
        (x + y) % k is constant.

        Args:
            nums: A list of integers.
            k: An integer, the modulus.

        Returns:
            The maximum length of a valid subsequence.

        The solution uses dynamic programming. dp[j][r] stores the maximum length of a valid
        subsequence ending at index j, where the constant remainder (x + y) % k is r.
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [[0] * k for _ in range(k)]
        ans = 0

        for j in range(n):
            for i in range(j):
                r = (nums[i] + nums[j]) % k
                # Either start a new pair (length = 2) or extend an existing subseq at i
                length = dp[i][r] + 1
                if length < 2:
                    length = 2
                if length > dp[j][r]:
                    dp[j][r] = length
                    if length > ans:
                        ans = length

        return ans