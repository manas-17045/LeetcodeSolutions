# Leetcode 3399: Smallest Substring With Identical Characters II
# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/
# Solved on 20th of June, 2025

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        """
        Finds the minimum possible length of the string `s` after performing at most `numOps` operations.

        An operation consists of changing a character at an index `i` to its opposite ('0' to '1' or '1' to '0').
        The goal is to make the string `s` such that every contiguous substring of length `k` contains at least
        one '0' and at least one '1'. This is equivalent to saying there are no runs of `k` or more identical characters.
        The problem asks for the minimum `k` such that we can achieve this condition with `numOps` or fewer operations.

        Args:
            s (str): The input binary string.
            numOps (int): The maximum number of operations allowed.
        """
        n = len(s)
        # Binary search on answer k
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.minOpsToLimit(s, mid) <= numOps:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def minOpsToLimit(self, s: str, k: int) -> int:
        n = len(s)
        # Special case k == 1: we need to make s fully alternating.
        if k == 1:
            # Count flips to make pattern '0101...' and '1010...'
            flips_start0 = 0
            for i, ch in enumerate(s):
                expected = '0' if (i % 2) == 0 else '1'
                if ch != expected:
                    flips_start0 += 1

            # Total mismatches to the other pattern is (n - flips_start0)
            flips_start1 = n - flips_start0
            return min(flips_start0, flips_start1)

        # General case k > 1: each run of length L needs floor (L/(k + 1)) flips
        ops = 0
        run_len = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                run_len += 1
            else:
                ops += run_len // (k + 1)
                run_len = 1
        ops += run_len // (k + 1)
        return ops