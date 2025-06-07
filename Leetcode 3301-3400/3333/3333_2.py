# Leetcode 3333: Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/
# Solved on 7th of June, 2025

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Calculates the number of possible strings that can be formed by extending
        each run of identical characters in the input word.

        For each run of identical characters of length L, we can extend it by
        adding x characters, where 0 <= x <= L - 1. The total number of added
        characters across all runs must be at least k minus the number of runs.

        Args:
            word: The input string.
            k: The minimum total number of added characters required.

        Returns:
            The number of possible strings modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # run-length encode
        runs = []
        prev = None
        cnt = 0
        for c in word:
            if c == prev:
                cnt += 1
            else:
                if cnt:
                    runs.append(cnt)
                prev = c
                cnt = 1
        if cnt:
            runs.append(cnt)

        R = len(runs)
        # We need sum(x_j) >= M.
        M = k - R

        # Product of (D_j+ 1) = L_j, used if M <= 0
        prod = 1
        for L in runs:
            prod = prod * L % MOD

        # If k <= R, the minimum sum of segments (all x_j = 0) already >= k,
        # so every choice of x_j is valid.
        if M <= 0:
            return prod

        # Otherwise, we have R < k, so R <= k - 1 and DP size M <= 2000.
        # dp[s] = #ways so far to have sum(x_j)=s, capped at s = M meaning ">=M"
        dp = [0] * (M + 1)
        dp[0] = 1

        for L in runs:
            d = L - 1
            # Build prefix sums of dp and of i*dp[i]
            pref = [0] * (M + 1)
            pref_i = [0] * (M + 1)
            s_acc = 0
            si_acc = 0
            for i in range(M + 1):
                s_acc = (s_acc + dp[i]) % MOD
                pref[i] = s_acc
                si_acc = (si_acc + dp[i] * i) % MOD
                pref_i[i] = si_acc

            dp2 = [0] * (M + 1)

            # For sums < M, we do a sliding-window sum over the last (d + 1) entries of dp
            for s in range(M):
                lo = s - d
                if lo <= 0:
                    dp2[s] = pref[s]
                else:
                    dp2[s] = (pref[s] - pref[lo - 1]) % MOD

            # For dp2[M], we need all ways that push us to >= M:
            # sum_{i=0...M} dp[i] * (# of x in [0...d] with i + x >= M)
            # = sum_{i=L0...M} dp[i] * ((i + d) - M + 1), where L0 = max(0, (M - d))
            L0 = max(0, (M - d))
            offset = M - d - 1
            if L0 > 0:
                sum_dp = (pref[M] - pref[L0 - 1]) % MOD
                sum_i = (pref_i[M] - pref_i[L0 - 1]) % MOD
            else:
                sum_dp = pref[M]
                sum_i = pref_i[M]

            dp2[M] = (sum_i - offset * sum_dp) % MOD

            dp = dp2

        # dp[M] now holds the total with sum >= M
        return dp[M] % MOD