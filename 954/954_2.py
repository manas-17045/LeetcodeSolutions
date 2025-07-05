# Leetcode 954: Array of Doubled Pairs
# https://leetcode.com/problems/array-of-doubled-pairs/
# Solved on 5th of July, 2025
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        """
        Given an array of integers arr of even length, return true if and only if it is possible to reorder it such
        that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.
        """
        cnt = Counter(arr)
        # Process numbers in increasing order of absolute value
        for x in sorted(cnt, key=abs):
            # If there aren't enough 2*x to pair with x, fail
            if cnt[x] > cnt[2 * x]:
                return False
            # Use up cnt[x] of the 2*x's
            cnt[2 * x] -= cnt[x]
        return True