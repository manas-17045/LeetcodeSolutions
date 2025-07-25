# Leetcode 2916: Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
# Solved on 25th of July, 2025
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        """
        Calculates the sum of (count_distinct(subarray))^2 for all subarrays of nums.
        This is achieved using a segment tree with lazy propagation to efficiently
        update and query the sum of distinct counts and their squares.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The total sum of squares of distinct counts, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7  # modulus for result
        n = len(nums)  # length of input
        size = 1
        while size < n:
            size <<= 1  # next power of two for segment tree
        seg_sum = [0] * (2 * size)  # segment tree for sums
        seg_sq = [0] * (2 * size)  # segment tree for sum of squares
        lazy = [0] * (2 * size)  # lazy propagation array

        def _apply(idx: int, length: int, v: int):
            # update sum of squares: a^2 -> (a+v)^2 = a^2 + 2av + v^2
            seg_sq[idx] = (seg_sq[idx] + 2 * v * seg_sum[idx] + v * v * length) % MOD
            seg_sum[idx] = (seg_sum[idx] + v * length) % MOD  # update sum
            lazy[idx] = (lazy[idx] + v) % MOD  # accumulate lazy tag

        def _push(idx: int, length: int):
            if lazy[idx]:
                half = length // 2
                _apply(idx * 2, half, lazy[idx])  # apply to left child
                _apply(idx * 2 + 1, half, lazy[idx])  # apply to right child
                lazy[idx] = 0  # clear tag

        def update(l: int, r: int, v: int, idx=1, left=0, right=None):
            if right is None:
                right = size - 1
            if l > right or r < left:  # no overlap
                return
            if l <= left and right <= r:  # total cover
                _apply(idx, right - left + 1, v)
                return
            _push(idx, right - left + 1)  # push before going down
            mid = (left + right) // 2
            update(l, r, v, idx * 2, left, mid)  # update left
            update(l, r, v, idx * 2 + 1, mid + 1, right)  # update right
            seg_sum[idx] = (seg_sum[idx * 2] + seg_sum[idx * 2 + 1]) % MOD  # pull up sum
            seg_sq[idx] = (seg_sq[idx * 2] + seg_sq[idx * 2 + 1]) % MOD  # pull up sum of squares

        last = {}  # last seen index for each value
        ans = 0  # accumulator for result
        for i, x in enumerate(nums):
            prev = last.get(x, -1)  # previous occurrence of x
            if prev + 1 <= i - 1:
                update(prev + 1, i - 1, 1)  # increment D[j] for j in (prev, i-1]
            update(i, i, 1)  # set D[i] = 1 for new subarray starting at i
            last[x] = i  # update last seen
            ans = (ans + seg_sq[1]) % MOD  # add total sum of squares at root
        return ans