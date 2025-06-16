# Leetcode 1713: Minimum Operations to Make a Subsequence
# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
# Solved on 16th of June, 2025
from bisect import bisect_left


class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        """
        Calculates the minimum number of operations to make arr a subsequence of target.

        An operation consists of inserting an element into arr. The problem is equivalent
        to finding the length of the longest common subsequence (LCS) between target and arr.
        The minimum number of operations is the length of target minus the length of the LCS.
        Since target has no duplicate elements, the LCS problem can be reduced to finding
        the longest increasing subsequence (LIS) of the indices of elements in arr that are
        also present in target.

        This solution uses patience sorting (tails array) to find the LIS in O(N log N) time,
        where N is the length of arr.
        """
        # Map each value in target to its index
        pos = {v: i for i, v in enumerate(target)}

        # Build the sequence of positions for elements in arr that are also in target
        seq = []
        for x in arr:
            if x in pos:
                seq.append(pos[x])

        # Find length of LIS in seq using patience sorting (tails)
        tails = []
        for idx in seq:
            i = bisect_left(tails, idx)
            if i == len(tails):
                tails.append(idx)
            else:
                tails[i] = idx

        # We need to insert the missing (target_len - LIS_len) elements.
        return len(target) - len(tails)