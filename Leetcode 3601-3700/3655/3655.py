# Leetcode 3655: XOR After Range Multiplication Queries II
# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/
# Solved on 20th of December, 2025
class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Applies a series of multiplication queries to elements of `nums` at specific intervals
        and then computes the XOR sum of the modified `nums`.

        Args:
            nums: A list of integers.
            queries: A list of queries, where each query is [l, r, k, v].
        Returns:
            The XOR sum of the modified `nums` after all queries are applied.
        """
        mod = 1000000007
        n = len(nums)
        b = int(n ** 0.5)

        totalMul = [1] * n
        smallQueries = [[] for _ in range(b + 1)]

        for l, r, k, v in queries:
            if k > b:
                for i in range(l, r + 1, k):
                    totalMul[i] = (totalMul[i] * v) % mod
            else:
                smallQueries[k].append((l, r, v))

        for k in range(1, b + 1):
            if not smallQueries[k]:
                continue

            diff = [1] * (n + b + 1)
            for l, r, v in smallQueries[k]:
                diff[l] = (diff[l] * v) % mod

                count = (r - l) // k
                nextIdx = l + (count + 1) * k

                if nextIdx < len(diff):
                    inv = pow(v, mod - 2, mod)
                    diff[nextIdx] = (diff[nextIdx] * inv) % mod

            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % mod
                totalMul[i] = (totalMul[i] * diff[i]) % mod

        result = 0
        for i in range(n):
            val = (nums[i] * totalMul[i]) % mod
            result ^= val

        return result