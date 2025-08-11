# Leetcode 2426: Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
# Solved on 12th of August, 2025
class BIT:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx: int, val: int) -> None:
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        """
        Calculates the number of pairs (i, j) such that i < j and nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff.
        Args:
            nums1 (list[int]): The first list of integers.
            nums2 (list[int]): The second list of integers.
            diff (int): The integer difference.
        Returns:
            int: The number of such pairs.
        """
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        OFFSET = 30001
        MAXV = 60010
        bit = BIT(MAXV)
        ans = 0
        for val in a:
            upper = val + diff + OFFSET
            ans += bit.query(upper)
            bit.update(val + OFFSET, 1)
        return ans