# Leetcode 1994: The Number of Good Subsets
# https://leetcode.com/problems/the-number-of-good-subsets/
# Solved on 10th of August, 2025
from collections import Counter


class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:

        MOD = 10 ** 9 + 7
        # Primes up to 30 (10 primes)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = Counter(nums)
        count1 = freq.get(1, 0)

        # Precompute mask for each value 2..30 if square-free (no p^2 divides it)
        val_mask = {}
        for v in range(2, 31):
            x = v
            mask = 0
            square_free = True
            for i, p in enumerate(primes):
                if x % p == 0:
                    cnt = 0
                    while x % p == 0:
                        x //= p
                        cnt += 1
                    if cnt > 1:
                        square_free = False
                        break
                    mask |= (1 << i)
            if square_free and x == 1:
                val_mask[v] = mask

        # DP over bitmasks of primes (10 primes -> 2^10 states)
        M = 1 << len(primes)
        dp = [0] * M
        dp[0] = 1  # empty selection of non-1 numbers

        # For each possible value (2..30) that is square-free and appears in nums
        for v, m in val_mask.items():
            c = freq.get(v, 0)
            if c == 0:
                continue
            # Iterate masks in reverse to avoid reusing the same value multiple times
            for old in range(M - 1, -1, -1):
                if dp[old] and (old & m) == 0:
                    dp[old | m] = (dp[old | m] + dp[old] * c) % MOD

        # Sum all non-empty prime-masks (subsets that actually include primes)
        total_nonempty = sum(dp[1:]) % MOD

        # Each subset can be combined with any subset of ones (2^count1 ways)
        pow2_ones = pow(2, count1, MOD)
        return (total_nonempty * pow2_ones) % MOD