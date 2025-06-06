# Leetcode 3261: Count Substrings That Satisfy K-Constraint II
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/
# Solved on 5th of June, 2025
from bisect import bisect_left
from collections import defaultdict


class FenwickTree:
    def __init__(self, sz):
        self.tr = [0] * (sz + 1)

    def update(self, i, d):
        i += 1
        while i < len(self.tr):
            self.tr[i] += d
            i += i & (-i)

    def query(self, i):
        i += 1
        sm = 0
        while i > 0:
            sm += self.tr[i]
            i -= i & (-i)
        return sm

    def queryRange(self, i, j):
        if i > j:
            return 0
        res = self.query(j)
        if i > 0:
            res -= self.query(i - 1)
        return res

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        """
        Counts the number of substrings within specified ranges that satisfy a k-constraint.

        A substring satisfies the k-constraint if the number of '0's and the number of '1's
        in the substring are both at most k.

        Args:
            s: The input string consisting of '0's and '1's.
            k: The maximum allowed count for '0's and '1's in a valid substring.
            queries: A list of queries, where each query is a list [l, r] representing
                     a range [l, r] (inclusive) in the string s.

        Returns:
            A list of integers, where the i-th element is the count of k-constraint substrings
            within the range specified by the i-th query.
        """
        n = len(s)

        pz = [0] * (n + 1)
        po = [0] * (n + 1)
        for i in range(n):
            pz[i + 1] = pz[i] + (1 if s[i] == '0' else 0)
            po[i + 1] = po[i] + (1 if s[i] == '1' else 0)

        end = [n] * n
        for i in range(n):
            targetZ = pz[i] + k
            posZ = bisect_left(pz, targetZ + 1, lo=i + 1)
            j0 = posZ - 1

            targetO = po[i] + k
            posO = bisect_left(po, targetO + 1, lo=i + 1)
            j1 = posO - 1

            end[i] = max(j0, j1)

        idxByV = defaultdict(list)
        for i in range(n):
            val = max(i, end[i])
            if val < n:
                idxByV[val].append(i)

        qByR = defaultdict(list)
        for qIdx, (l, r) in enumerate(queries):
            qByR[r].append((l, qIdx))

        ans = [0] * len(queries)
        bitCnt = FenwickTree(n)
        bitSum = FenwickTree(n)

        for rIdx in range(n):
            for i in idxByV[rIdx]:
                bitCnt.update(i, 1)
                bitSum.update(i, rIdx)

            for l, qIdx in qByR[rIdx]:
                actCnt = bitCnt.queryRange(l, rIdx)
                sumV = bitSum.queryRange(l, rIdx)

                badCnt = (rIdx + 1) * actCnt - sumV

                length = rIdx - l + 1
                totalSubs = length * (length + 1) // 2

                ans[qIdx] = totalSubs - badCnt

        return ans