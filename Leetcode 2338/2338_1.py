# Leetcode 2338: Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

MOD = 10 ** 9 + 7

MAX_COMB_N = 10000 + 15

fact = [1] * MAX_COMB_N
inv_fact = [1] * MAX_COMB_N

for i in range(1, MAX_COMB_N):
    fact[i] = (fact[i - 1] * i) % MOD

inv_fact[MAX_COMB_N - 1] = pow(fact[MAX_COMB_N - 1], MOD - 2, MOD)

for i in range(MAX_COMB_N - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD


def nCr_mod(n_comb, r_comb):
    """
    Computes combinations (nCr) modulo MOD using precomputed factorials and inverses.
    Handles combinations C(n, r).
    """

    if r_comb < 0 or r_comb > n_comb or n_comb < 0:
        return 0

    if n_comb >= MAX_COMB_N:
        raise ValueError(f"nCr argument n_comb={n_comb} exceeds precomputed range {MAX_COMB_N}")

    if r_comb == 0 or r_comb == n_comb:
        return 1

    if r_comb > n_comb // 2:
        r_comb = n_comb - r_comb

    numerator = fact[n_comb]
    denominator = (inv_fact[r_comb] * inv_fact[n_comb - r_comb]) % MOD

    return (numerator * denominator) % MOD


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        global fact, inv_fact, MOD, MAX_COMB_N

        max_e = 0
        if maxValue > 1:
            max_e = maxValue.bit_length()

        ways = [1] * (max_e + 1)
        inv_ways = [1] * (max_e + 1)
        ways[0] = 1
        inv_ways[0] = 1

        for e in range(1, max_e + 1):
            comb_val = nCr_mod(e + n - 1, e)
            ways[e] = comb_val
            inv_ways[e] = pow(comb_val, MOD - 2, MOD)

        f = [1] * (maxValue + 1)

        is_prime = [True] * (maxValue + 1)
        if maxValue >= 0: is_prime[0] = False
        if maxValue >= 1: is_prime[1] = False

        for p in range(2, maxValue + 1):
            if is_prime[p]:
                pe = p
                e = 1
                while pe <= maxValue:
                    factor = (ways[e] * inv_ways[e - 1]) % MOD

                    for v in range(pe, maxValue + 1, pe):
                        if v != p:
                            is_prime[v] = False
                        f[v] = (f[v] + factor) % MOD

                        e += 1

                        if p > maxValue // pe:
                            break
                        pe *= p

        total_sum = sum(f[i] for i in range(1, maxValue + 1)) % MOD
        return total_sum