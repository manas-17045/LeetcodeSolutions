# Leetcode 2817: Minimum Absolute Difference Between Elements With Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/
# Solved on 24th of June, 2025
class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.fw = [0] * (n + 1)
        self._max_pow2 = 1
        while self._max_pow2 << 1 <= n:
            self._max_pow2 <<= 1

    def add(self, i: int, v: int):
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def find_kth(self, k: int) -> int:
        idx = 0
        bit_mask = self._max_pow2
        while bit_mask:
            t = idx + bit_mask
            if t <= self.n and self.fw[t] < k:
                idx = t
                k -= self.fw[t]
            bit_mask >>= 1
        return idx + 1


class Solution:
    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        """
        Calculates the minimum absolute difference between two elements nums[i] and nums[j]
        such that abs(i - j) >= x.

        The solution uses a Fenwick tree (Binary Indexed Tree) to efficiently find
        predecessors and successors of elements.

        Args:
            nums: A list of integers.
            x: An integer representing the minimum absolute difference between indices.

        Returns:
            The minimum absolute difference found.
        """
        n = len(nums)
        # Compress values
        sa = sorted(set(nums))
        m = len(sa)
        comp = {v: (i + 1) for i, v in enumerate(sa)}  # 1-based

        bit = Fenwick(m)
        ans = 10**18

        # Process i = x...(n - 1)
        for i in range(x, n):
            r0 = comp[nums[i - x]]
            bit.add(r0, 1)

            v = nums[i]
            r = comp[v]

            cnt_le = bit.sum(r)
            if cnt_le > 0:
                predRank = bit.find_kth(cnt_le)
                ans = min(ans, (v - sa[predRank - 1]))
                if ans == 0:
                    return 0
            total = bit.sum(m)
            if cnt_le < total:
                succRank = bit.find_kth(cnt_le + 1)
                ans = min(ans, (sa[succRank - 1] - v))
                if ans == 0:
                    return 0

        return ans