# Leetcode 3261: Count Substrings That Satisfy K-Constraint II
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/
# Solved on 5th of June, 2025
from bisect import bisect_left


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        """
        Counts the number of substrings within specified ranges [l, r] that satisfy the k-constraint.
        A substring satisfies the k-constraint if the number of '0's and '1's in it are both at most k.

        Args:
            s: The input binary string.
            k: The maximum allowed count for '0's and '1's in a valid substring.
            queries: A list of query ranges [l, r].

        Returns:
            A list of integers, where each element is the count of k-constraint substrings for the corresponding query.
        """
        n = len(s)
        # Build prefix-sum arrays for zeroes and ones
        prefixZeroes = [0] * (n + 1)
        prefixOnes = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefixZeroes[i + 1] = prefixZeroes[i] + (1 if ch == '0' else 0)
            prefixOnes[i + 1] = prefixOnes[i] + (1 if ch == '1' else 0)

        bs = [n] * n
        for i in range(n):
            tz = prefixZeroes[i] + k + 1
            idx0 = bisect_left(prefixZeroes, tz)
            j0 = idx0 - 1 if idx0 <= n else n

            to = prefixOnes[i] + k + 1
            idx1 = bisect_left(prefixOnes, to)
            j1 = idx1 - 1 if idx1 <= n else n

            limit = max(j0, j1)
            if limit < i:
                limit = i
            bs[i] = limit

        by_bs = [[] for _ in range(n + 1)]
        for i in range(n):
            if bs[i] <= n:
                by_bs[bs[i]].append(i)

        class Fenwick:
            def __init__(self, size: int):
                self.n = size
                self.data = [0] * (size + 1)

            def update(self, idx: int, val: int):
                # All val to position idx (0-based)
                i = idx + 1
                while i <= self.n:
                    self.data[i] += val
                    i += (i & -i)

            def query(self, idx: int) -> int:
                # Sum of [0...idx] inclusive
                i = idx + 1
                s = 0
                while i > 0:
                    s += self.data[i]
                    i -= (i & -i)
                return s

            def rangeSum(self, left: int, right) -> int:
                if left > right:
                    return 0
                return self.query(right) - (self.query(left - 1) if left > 0 else 0)

        BIT_count = Fenwick(n)
        BIT_sumBs = Fenwick(n)

        # Group queries by r. We will process them in increasing order of r.
        queriesByR = [[] for _ in range(n)]
        for qi, (l, r) in enumerate(queries):
            queriesByR[r].append((l, qi))

        answers = [0] * len(queries)

        for R in range(n):
            for i in by_bs[R]:
                BIT_count.update(i, 1)
                BIT_sumBs.update(i, bs[i])

            # Answer each query [l, R]
            for (l, qIdx) in queriesByR[R]:
                length = R - l + 1
                totalSubs = length * (length + 1) // 2

                cnt = BIT_count.rangeSum(l, R)

                sumBSInRange = BIT_sumBs.rangeSum(l, R)

                invalids = cnt * (R + 1) - sumBSInRange
                answers[qIdx] = totalSubs - invalids

        return answers