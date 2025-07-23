# Leetcode 3277: Maximum XOR Score Subarray Queries
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/
# Solved on 23rd of July, 2025
class Solution:
    def maximumSubarrayXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the maximum XOR sum of subarrays for given queries.

        Args:
            nums (list[int]): The input array of integers.
            queries (list[list[int]]): A list of queries, where each query [l, r] represents a subarray from index l to r (inclusive).
        Returns:
            list[int]: A list of integers, where each element is the maximum XOR sum for the corresponding query.
        """
        n = len(nums)

        score = [[0] * n for _ in range(n)]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            score[i][i] = nums[i]
            dp[i][i] = nums[i]

        for length in range(2, (n + 1)):
            for i in range(n - length + 1):
                j = i + length - 1
                # XOR-score recurrence
                score[i][j] = score[i][j - 1] ^ score[i + 1][j]
                dp[i][j] = max(score[i][j], dp[i][j - 1], dp[i + 1][j])

        return [dp[l][r] for l, r in queries]