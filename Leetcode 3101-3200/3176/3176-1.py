# Leetcode 3176: Find the Maximum Length of a Good Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/
# Solved on 26th of September, 2025
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum length of a "good" subsequence.

        A subsequence is "good" if the number of pairs of adjacent elements
        in the subsequence with different values is at most k.
        :param nums: A list of integers.
        :param k: The maximum allowed number of different adjacent elements.
        :return: The maximum length of a good subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [{} for _ in range(k + 1)]

        max_len_at_j = [0] * (k + 1)

        for x in nums:
            for j in range(k, -1, -1):
                len_same_val = 1 + dp[j].get(x, 0)

                len_diff_val = 0
                if j > 0:
                    len_diff_val = 1 + max_len_at_j[j - 1]

                new_len = max(len_same_val, len_diff_val)

                dp[j][x] = new_len

                max_len_at_j[j] = max(max_len_at_j[j], new_len)

        return max(max_len_at_j) if max_len_at_j else 0