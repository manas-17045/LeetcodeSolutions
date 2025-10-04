# Leetcode 3165: Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
# Solved on 4th of October, 2025
import sys
sys.setrecursionlimit(100000)


class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Calculates the maximum sum of a subsequence with non-adjacent elements after a series of updates.

        Args:
            nums: A list of integers representing the initial array.
            queries: A list of lists, where each inner list `[pos, val]` represents an update
                     to `nums[pos]` with the new value `val`.

        Returns:
            The total sum of maximum subsequence sums after each query, modulo 10^9 + 7.
        """
        self.n = len(nums)
        self.nums = nums
        self.tree = [()] * (4 * self.n)
        self.negInf = -float('inf')
        self.mod = 10 ** 9 + 7

        if self.n > 0:
            self._build(1, 0, self.n - 1)

        totalSum = 0
        for pos, val in queries:
            if self.n == 0:
                totalSum = (totalSum + 0) % self.mod
                continue

            self._update(1, 0, self.n - 1, pos, val)

            rootNode = self.tree[1]
            maxSum = max(0, rootNode[0], rootNode[1], rootNode[2], rootNode[3])
            totalSum = (totalSum + maxSum) % self.mod

        return totalSum

    def _merge(self, left, right):
        # States: sumEE, sumEI, sumIE, sumII
        # (Exclude-Exclude, Exclude-Include, Include-Exclude, Include-Include)
        lee, lei, lie, lii = left
        ree, rei, rie, rii = right

        # Max sum excluding both new endpoints
        pee = max(lee, lei, ree, rie, lei + ree, lee + rie, lee + ree)

        # Max sum excluding left endpoint, including right endpoint
        pei = max(rei, rii, lei + rei, lee + rii, lee + rei)

        # Max sum including left endpoint, excluding right endpoint
        pie = max(lie, lii, lii + ree, lie + rie, lie + ree)

        # Max sum including both new endpoints
        pii = max(lii + rei, lie + rii, lie + rei)

        return (pee, pei, pie, pii)

    def _build(self, nodeIndex, start, end):
        if start == end:
            self.tree[nodeIndex] = (0, self.negInf, self.negInf, self.nums[start])
            return

        mid = start + (end - start) // 2
        leftChild = 2 * nodeIndex
        rightChild = 2 * nodeIndex + 1

        self._build(leftChild, start, mid)
        self._build(rightChild, mid + 1, end)

        self.tree[nodeIndex] = self._merge(self.tree[leftChild], self.tree[rightChild])

    def _update(self, nodeIndex, start, end, idx, val):
        if start == end:
            self.nums[idx] = val
            self.tree[nodeIndex] = (0, self.negInf, self.negInf, val)
            return

        mid = start + (end - start) // 2
        leftChild = 2 * nodeIndex
        rightChild = 2 * nodeIndex + 1

        if start <= idx <= mid:
            self._update(leftChild, start, mid, idx, val)
        else:
            self._update(rightChild, mid + 1, end, idx, val)

        self.tree[nodeIndex] = self._merge(self.tree[leftChild], self.tree[rightChild])
