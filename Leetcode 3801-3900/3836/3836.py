# Leetcode 3836: Maximum Score Using Exactly K Pairs
# https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/
# Solved on 10th of February, 2026
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Calculates the maximum score possible by selecting exactly k pairs of elements
        from nums1 and nums2 while maintaining their relative order.

        :param nums1: List of integers representing the first sequence.
        :param nums2: List of integers representing the second sequence.
        :param k: The exact number of pairs to be formed.
        :return: The maximum total score as an integer.
        """
        n = len(nums1)
        m = len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for l in range(1, k + 1):
            curr = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    match = dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]
                    skip1 = curr[i - 1][j]
                    skip2 = curr[i][j - 1]
                    curr[i][j] = max(match, skip1, skip2)

            dp = curr

        return int(dp[n][m])