# Leetcode 2659: Make Array Empty
# https://leetcode.com/problems/make-array-empty/
# Solved on 7th of June, 2025

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.fw = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i

    def prefixSum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def rangeSum(self, l: int, r: int) -> int:
        return self.prefixSum(r) - self.prefixSum(l - 1)

class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        """
        Calculates the total number of operations to empty an array by repeatedly
        finding the smallest element, removing it, and counting the elements
        between the current "first" element and the removed element, wrapping
        around if necessary.

        Args:
            nums: A list of integers.

        Returns:
            The total number of operations.
        """
        n = len(nums)
        # Memoize original positions (0-based -> we'll use 1-based iin Fenwick)
        pos = {v: i for i, v in enumerate(nums)}
        # Prepare Fenwick tree: all positions initially "occupied" (count = 1)
        fw = Fenwick(n)
        for i in range(1, n + 1):
            fw.add(i, 1)

        # Our "first element" pointer in [1...n]
        cur = 1
        ops = 0
        # Process values in ascending order
        for v in sorted(nums):
            # 1-based
            p = pos[v] + 1
            if p >= cur:
                # No wrap
                cnt = fw.rangeSum(cur, p)
            else:
                # Wrap around end -> start
                cnt = fw.rangeSum(cur, n) + fw.rangeSum(1, p)
            ops += cnt

            # Remove this element
            fw.add(p, -1)
            # Next, "first" is the position we just removed
            cur = p

        return ops