# Leetcode 3398: Smallest Substring With Identical Characters I
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/
# Solved on 29th of May, 2025

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        """
        Finds the smallest possible length L such that the string s can be transformed
        into a string consisting of only '0's or only '1's, where each character
        appears in a run of length at least L, using at most numOps flips.

        Args:
            s: The input binary string.
            numOps: The maximum number of flips allowed.
        """
        n = len(s)
        # Convert to int for speed
        A = [1 if c == '1' else 0 for c in s]

        def feasible(L: int) -> bool:
            # dp0[j] = min flips to build prefix ending in a run of 0's of length j
            # dp1[j] = same for a run of 1's of length j
            INF = numOps + 1
            dp0 = [INF] * (L + 2)
            dp1 = [INF] * (L + 2)
            # Base at i = 0
            dp0[1] = (A[0] != 0)
            dp1[1] = (A[0] != 1)

            for i in range(1, n):
                new0 = [INF] * (L + 2)
                new1 = [INF] * (L + 2)
                flip0 = (A[i] != 0)
                flip1 = (A[i] != 1)

                # Extend or switch to 0
                # Extend from a shorter run of 0's
                for j in range(1, L):
                    v = dp0[j]
                    if v <= numOps:
                        new0[j + 1] = v + flip0
                # Switch from any 1-run
                best1 = min(dp1[1:L + 1])
                if best1 <= numOps:
                    new0[1] = best1 + flip0

                # Extend or switch to 1
                for j in range(1, L):
                    v = dp1[j]
                    if v <= numOps:
                        new1[j + 1] = v + flip1
                best0 = min(dp0[1:L + 1])
                if best0 <= numOps:
                    new1[1] = best0 + flip1

                dp0, dp1 = new0, new1

            # Check if any ending-state is within budget
            return min(min(dp0[1:L + 1]), min(dp1[1:L + 1])) <= numOps

        # Binary Search smallest L in [1...n]
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo