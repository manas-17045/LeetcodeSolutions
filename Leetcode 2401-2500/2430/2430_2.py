# Leetcode 2430: Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/
# Solved on 28th of July, 2025
class Solution:
    def deleteString(self, s: str) -> int:
        """
        Calculates the maximum number of operations to delete the entire string.
        :param s: The input string.
        :return: The maximum number of deletions.
        """
        n = len(s)
        # dp[i] = maximum deletions to clear s[i:]
        dp = [0] * (n + 1)
        # lcp_next[j] = LCP length of suffixes starting at i+1 and j, for the previous i+1 row
        lcp_next = [0] * (n + 1)

        # Process from the end backward
        for i in range(n - 1, -1, -1):
            # At worst, we delete the entire suffix s[i:]
            best = 1
            # Compute the LCP row for i vs. all j > i
            lcp_curr = [0] * (n + 1)
            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    lcp_curr[j] = 1 + lcp_next[j + 1]
            # Try all valid "double-prefix" deletions of length k.
            half = (n - i) // 2
            for k in range(1, half + 1):
                if lcp_curr[i + k] >= k:
                    # We can delete the first k chars, then solve from i+k
                    best = max(best, 1 + dp[i + k])
            dp[i] = best
            # Move current LCP row into next for the next iteration
            lcp_next = lcp_curr

        return dp[0]