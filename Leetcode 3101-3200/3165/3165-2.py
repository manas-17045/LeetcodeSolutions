# Leetcode 3165: Maximum Sum of Subsequence With Non-adjacent Elements
# https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
# Solved on 4th of October, 2025
class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Calculates the sum of maximum sum subsequences after each query.
        :param nums: A list of integers representing the initial array.
        :param queries: A list of queries, where each query is [pos, x] meaning nums[pos] is updated to x.
        :return: The total sum of maximum sum subsequences modulo 10^9 + 7 after each query.
        """
        MOD = 10 ** 9 + 7
        NEG_INF = -10 ** 18

        n = len(nums)
        # Segment tree storing 2x2 matrices as tuples (m00, m01, m10, m11)
        # row0 = [m00, m01], row1 = [m10, m11]
        size = 1
        while size < n:
            size <<= 1
        seg = [(0, 0, NEG_INF, NEG_INF)] * (2 * size)  # initialize

        def leaf_matrix(v: int):
            # [[0,0],[v,-inf]]
            return (0, 0, v, NEG_INF)

        def mat_mul(A, B):
            # C = A * B where C[i][j] = max_k (A[i][k] + B[k][j])
            a00, a01, a10, a11 = A
            b00, b01, b10, b11 = B
            c00 = max(a00 + b00, a01 + b10)
            c01 = max(a00 + b01, a01 + b11)
            c10 = max(a10 + b00, a11 + b10)
            c11 = max(a10 + b01, a11 + b11)
            return (c00, c01, c10, c11)

        # Build leaves
        for i in range(n):
            seg[size + i] = leaf_matrix(nums[i])
        for i in range(size - 1, 0, -1):
            left = seg[2 * i]
            right = seg[2 * i + 1]
            # combined = right * left (left segment followed by right)
            seg[i] = mat_mul(right, left)

        def point_update(pos: int, v: int):
            i = size + pos
            seg[i] = leaf_matrix(v)
            i //= 2
            while i:
                left = seg[2 * i]
                right = seg[2 * i + 1]
                seg[i] = mat_mul(right, left)
                i //= 2

        total = 0
        for pos, x in queries:
            point_update(pos, x)
            root = seg[1]
            # Apply root to prev = [0, -inf] -> final0 = root[0][0], final1 = root[1][0]
            best = max(root[0], root[2])
            if best < 0:
                best = 0  # empty subsequence allowed (though DP already handles this)
            total = (total + (best % MOD)) % MOD

        return total