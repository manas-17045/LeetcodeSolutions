# Leetcode 3130: Find All Possible Stable Binary Arrays II
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/
# Solved on 12th of July, 2025
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        Calculates the number of stable arrays given counts of zeros and ones, and a limit on consecutive identical characters.

        A stable array is one where no more than 'limit' consecutive identical characters appear.

        Args:
            zero (int): The total number of zeros available.
            one (int): The total number of ones available.
            limit (int): The maximum number of consecutive identical characters allowed.

        Returns:
            int: The total number of stable arrays modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        def build_dp(target: int):
            dp_prev = [0] * (target + 1)
            dp_prev[0] = 1
            dp_k_val = [0] * (target + 1)
            dp_k_val[0] = 1 if target == 0 else 0

            for k in range(1, (target + 1)):
                dp_curr = [0] * (target + 1)
                pref = [0] * (target + 1)
                running = 0
                for s in range(target + 1):
                    running = (running + dp_prev[s]) % MOD
                    pref[s] = running
                for n in range(1, (target + 1)):
                    low = n - limit
                    if low > 0:
                        dp_curr[n] = (pref[n - 1] - pref[low - 1]) % MOD
                    else:
                        dp_curr[n] = pref[n - 1] % MOD
                dp_k_val[k] = dp_curr[target]
                dp_prev = dp_curr

            return dp_k_val

        # Build tables for zeros and ones
        dp0 = build_dp(zero)
        dp1 = build_dp(one)

        total = 0
        # Sequences starting with 0: for each number f zero-blocks b0 >= 1
        for b0 in range(1, (zero + 1)):
            zWays = dp0[b0]
            if not zWays:
                continue
            b1 = b0 - 1
            if 0 <= b1 <= one:
                total = (total + zWays * dp1[b1]) % MOD
            b1 = b0
            if 0 <= b1 <= one:
                total = (total + zWays * dp1[b1]) % MOD

        # Sequences starting with 1: for each number of one blocks b1 >= 1
        for b1 in range(1, (one + 1)):
            oWays = dp1[b1]
            if not oWays:
                continue
            b0 = b1 - 1
            if 0 <= b0 <= zero:
                total = (total + oWays * dp0[b0]) % MOD
            b0 = b1
            if 0 <= b0 <= zero:
                total = (total + oWays * dp0[b0]) % MOD

        return total