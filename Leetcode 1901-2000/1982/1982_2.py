# Leetcode 1982: Find Array Given Subset Sums
# https://leetcode.com/problems/find-array-given-subset-sums/
# Solved on 5th of July, 2025
from collections import Counter


class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        """
        Given an integer n and an array sums, where sums[i] is the sum of a subset of elements from an unknown array of n integers,
        return the unknown array.

        The input array sums contains 2^n integers, representing all possible subset sums of the unknown array.
        The order of elements in sums is not guaranteed.
        The unknown array can contain both positive and negative integers.

        Args:
            n (int): The number of elements in the unknown array.
            sums (list[int]): A list of 2^n subset sums.
        Returns:
            list[int]: The recovered unknown array.
        """
        # Recursive helper: given the multiset of subset-sums, recover one ordering
        def helper(subs: list[int]) -> list[int]:
            if len(subs) == 1:
                # Only the empty-subset sum remains
                return []

            subs.sort()
            delta = subs[1] - subs[0]   # Candidate element value (or its negation)
            cnt = Counter(subs)

            excl, incl = [], []     # Will jold the two halves of the multiset
            for s in subs:
                if cnt[s] == 0:
                    continue
                # Match s (without x) with s + delta (with x)
                cnt[s] -= 1
                cnt[s + delta] -= 1
                excl.append(s)
                incl.append(s + delta)

            if 0 in incl:
                return helper(incl) + [-delta]
            else:
                return helper(excl) + [delta]

        return helper(sums)