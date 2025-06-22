# Leetcode 1923: Longest Common Subpath
# https://leetcode.com/problems/longest-common-subpath/
# Solved on 22nd of June, 2025
import random


class Solution:
    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        """
        Finds the length of the longest common subpath among all given paths.

        A subpath is a contiguous sequence of nodes within a path.
        A common subpath is a subpath that appears in every path.

        This problem is solved using a combination of binary search on the
        length of the subpath and a Rabin-Karp rolling hash algorithm
        to efficiently check for common subpaths of a given length.

        Args:
            n: The number of distinct nodes (not directly used in the solution logic,
               but part of the problem statement context).
            paths: A list of lists, where each inner list represents a path of nodes.
        """
        # Mersenne Prime (2^61-1) for rolling hash
        MOD = (1 << 61) - 1

        def _modmul(a: int, b: int) -> int:
            prod = a * b

            low = prod & MOD
            high = prod >> 61
            x = low + high

            if x >= MOD:
                x -= MOD
            return x

        base= random.randrange(10**5, MOD)

        min_len = min(len(p) for p in paths)

        power = [1] * (min_len + 1)

        for i in range(1, (min_len + 1)):
            power[i] = _modmul(power[i - 1], base)

        def hasCommon(L: int) -> bool:
            commonHashes = None

            for path in paths:
                h = 0
                seen = set()

                for x in path[:L]:
                    h = _modmul(h, base) + x
                    if h >= MOD:
                        h -= MOD
                seen.add(h)

                # Roll over the rest
                for i in range(L, len(path)):
                    h = _modmul(h, base) + path[i]
                    if h >= MOD:
                        h -= MOD

                    rem = _modmul(path[i - L], power[L])
                    h -= rem
                    if h < 0:
                        h += MOD
                    seen.add(h)

                if commonHashes is None:
                    commonHashes = seen
                else:
                    commonHashes &= seen
                    if not commonHashes:
                        return False

            return True

        # Binary search over length L
        lo, hi, ans = 1, min_len, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if hasCommon(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans