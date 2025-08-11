# Leetcode 2926: Maximum Balanced Subsequence Sum
# https://leetcode.com/problems/maximum-balanced-subsequence-sum/
# Solved on 11th of August, 2025
class Fenwick:
    def __init__(self, size: int):
        self.size = size
        self.tree = [-10**18] * (size + 1)

    def update(self, index: int, value: int):
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)
            index += index & -index

    def query(self, index: int) -> int:
        res = -10**18
        while index > 0:
            res = max(res, self.tree[index])
            index -= index & -index

        return res

class Solution:
    def maxBalancedSubsequenceSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum balanced subsequence sum.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The maximum balanced subsequence sum.
        """
        if not nums:
            return 0
        n = len(nums)
        vals = [nums[i] - i for i in range(n)]
        unique = sorted(set(vals))
        rank = {v: i + 1 for i, v in enumerate(unique)}
        m = len(unique)
        ft = Fenwick(m)
        maxSum = -10**18
        for i in range(n):
            v = vals[i]
            r = rank[v]
            prev = ft.query(r)
            add = 0 if prev == -10**18 else prev
            curr = nums[i] + add
            maxSum = max(maxSum, curr)
            if curr > 0:
                ft.update(r, curr)

        return maxSum