# Leetcode 1735: Count Ways to Make Array With Product
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# Solved on 22nd of July, 2025
class Solution:
    def waysToFillAray(self, queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of ways to fill an array with `n` positive integers such that their product is `k`.

        Args:
            queries: A list of lists, where each inner list `[n, k]` represents a query.
        Returns:
            A list of integers, where each element is the answer to the corresponding query modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Scan to get limits
        max_n = 0
        max_k = 0
        for n, k in queries:
            if n > max_n:
                max_n = n
            if k > max_k:
                max_k = k

        # Build smallest-prime-factor sieve up to max_k
        spf = list(range(max_k + 1))
        for p in range(2, int(max_k**0.5) + 1):
            if spf[p] == p:
                for multiple in range(p * p, max_k + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # Precompute factorials & inv-factorials up to max_n + margin
        LIM = max_n + 100
        fac = [1] * (LIM + 1)
        for i in range(1, LIM + 1):
            fac[i] = fac[i - 1] * i % MOD
        inv_fac = [1] * (LIM + 1)
        inv_fac[LIM] = pow(fac[LIM], MOD - 2, MOD)
        for i in range(LIM, 0, -1):
            inv_fac[i - 1] = inv_fac[i] * i % MOD

        def comb(a: int, b: int) -> int:
            return fac[a] * inv_fac[b] * MOD * inv_fac[a - b] % MOD

        # Answer each query
        ans = []
        for n, k in queries:
            res = 1
            # Factor k by repeatedly pulling off spf
            x = k
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                res = res * comb(cnt + n - 1, n - 1) % MOD

            ans.append(res)

        return ans