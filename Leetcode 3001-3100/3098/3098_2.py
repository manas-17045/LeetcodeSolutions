# Leetcode 3098: Find the Sum of Subsequence Powers
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/
# Solved on 29th of June, 2025
class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of powers of all possible subsequences of length k.
        The "power" of a subsequence is defined as the minimum difference between any two elements in the subsequence.

        Args:
            nums: A list of integers.
            k: The desired length of the subsequences.
        Returns:
            The sum of powers of all valid subsequences, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)
        a = sorted(nums)
        # Build sorted list of all distinct a[j] - a[i]
        diffs = set()
        for i in range(n):
            for j in range(i + 1, n):
                diffs.add(a[j] - a[i])
        D = sorted(diffs)

        # Helper function
        def count_at_least(m: int) -> int:
            # p[i] = largest index < i such that a[i] - a[p[i]] > m
            p = [-1] * n
            l = 0
            for i in range(n):
                # Advance l such that a[i] - a[l] < m, then valid are <= (l - 1).
                while l < i and a[i] - a[l] >= m:
                    l += 1
                p[i] = l - 1

            # dp[j][i]: ways to pick j elements ending at i
            # Roll over j; for j = 1: dp = [1] * n
            dp_prev = [1] * n
            for length in range(2, (k + 1)):
                # Build prefix sums of dp_prev
                prefix = [0] * n
                prefix[0] = dp_prev[0]
                for i in range(1, n):
                    prefix[i] = (prefix[i - 1] + dp_prev[i]) % MOD
                dp_cur = [0] * n
                for i in range(n):
                    if p[i] >= 0:
                        dp_cur[i] = prefix[p[i]]
                dp_prev = dp_cur

            return sum(dp_prev) % MOD

        # For each threshold in ascending order compute f
        F = [count_at_least(m) for m in D]
        # F is non-increasing => number with exact min = F[i] - F[i + 1]
        ans = 0
        for i, m in enumerate(D):
            if (i + 1) < len(D):
                cnt = (F[i] - F[i + 1]) % MOD
            else:
                cnt = F[i]
            ans = (ans + m * cnt) % MOD

        return ans