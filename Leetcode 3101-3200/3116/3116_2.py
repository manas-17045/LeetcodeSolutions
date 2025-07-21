# Leetcode 3116: Kth Smallest Amount With Single Denomination Combination
# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
# Solved on 21st of July, 2025
import math


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        """
        Finds the k-th smallest positive integer that is divisible by at least one coin in the given list.
        :param coins: A list of integers representing the available coin denominations.
        :param k: The k-th smallest number to find.
        :return: The k-th smallest positive integer divisible by at least one coin.
        """
        n = len(coins)
        # Precompute LCMs for every non-empty subset of coins
        N = 1 << n
        lcms = [0] * N
        lcms[0] = 1
        for mask in range(1, N):
            # Isolate lowest set bit
            i = (mask & -mask).bit_length() - 1
            prev = mask ^ (1 << i)
            a, b = lcms[prev], coins[i]
            g = math.gcd(a, b)
            lcms[mask] = a // g * b

        sign = [1 if bin(mask).count('1') & 1 else -1 for mask in range(N)]

        def count_upto(x: int) -> int:
            tot = 0
            for mask in range(1, N):
                d = lcms[mask]
                if d <= x:
                    tot += sign[mask] * (x // d)
            return tot

        # Binary search on answer in [1, k * min(coins)]
        low, high = 1, k * min(coins)
        while low < high:
            mid = (low + high) // 2
            if count_upto(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low