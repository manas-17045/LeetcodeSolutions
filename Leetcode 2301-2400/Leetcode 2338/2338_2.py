# Leetcode 2338: Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

import math

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        M = maxValue

        divisors = [[] for _ in range(M + 1)]
        for d in range(1, M):
            for m in range(d * 2, M + 1, d):
                divisors[m].append(d)

        Lmax = min(n, int(math.log2(M)) + 1)

        dp_prev = [1] * (M + 1)
        sumChains = [0] * (Lmax + 1)
        sumChains[1] = M

        for length in range(2, Lmax + 1):
            dp_curr = [0] * (M + 1)
            # only k >= 2 have proper divisors
            for k in range(2, M + 1):
                for d in divisors[k]:
                    dp_curr[k] = (dp_curr[k] + dp_prev[d]) % MOD
            dp_prev = dp_curr
            # total number of strict chains of this length
            sumChains[length] = sum(dp_curr) % MOD

        comb = [0] * (Lmax + 1)
        comb[1] = 1
        inv = [0] * (Lmax + 1)
        if Lmax >= 1:
            inv[1] = 1
        # compute modular inverses via linear method
        for i in range(2, Lmax + 1):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        # build combs
        for length in range(2, Lmax + 1):
            # C(n-1, length-1) = C(n-1, (length-1)-1) * ((n-1) - ((length-1)-1)) / (length-1)
            comb[length] = comb[length - 1] * (n - (length - 1)) % MOD * inv[length - 1] % MOD

        ans = 0
        for length in range(1, Lmax + 1):
            ans = (ans + sumChains[length] * comb[length]) % MOD
        return ans