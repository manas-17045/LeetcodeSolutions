# Leetcode 3343: Count Number of Balanced Permutations
# https://leetcode.com/problems/count-number-of-balanced-permutations/

from collections import defaultdict


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        """
        This function calculates the number of distinct balanced permutations of a given numeric string. A
        balanced permutation is defined as one where the sum of the digits in the first half of the permutation
        equals the sum of the digits in the second half. The function employs combinatorics and dynamic programming
        to count the number of valid permutations efficiently under the constraint of a large modulo value.

        :param num: A string of digits representing the numeric input for which balanced permutations need to be counted.
        :type num: str
        :return: The count of balanced permutations of the given numeric string modulo 10^9 + 7.
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        N = len(num)

        original_counts = defaultdict(int)
        total_sum_digits = 0
        for digit_char in num:
            digit_val = int(digit_char)
            original_counts[digit_val] += 1
            total_sum_digits += digit_val

        if total_sum_digits % 2 != 0:
            return 0

        S_target = total_sum_digits // 2
        N_e = (N + 1) // 2
        N_o = N //2

        fact = [1] * (N + 1)
        invfact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        # Fermat's Little Theorem for inverse
        invfact[N] = pow(fact[N], MOD - 2, MOD)
        # invfact[0] will correctly become 1
        for i in range(N - 1, -1, -1):
            invfact[i] = (invfact[i + 1] * (i + 1)) % MOD

        def nCr_mod(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            numerator = fact[n_val]
            denominator = (invfact[r_val] * invfact[n_val - r_val]) % MOD
            return (numerator * denominator) % MOD

        dp = [[0] * (S_target + 1) for _ in range(N_e + 1)]
        # Base case: 0 items sum to 0 in 1 way (empty product of binomials = 1)
        dp[0][0] = 1

        # For each digit type 0-9
        for d_val in range(10):
            C_d = original_counts[d_val]

            new_dp = [[0] * (S_target + 1) for _ in range(N_e + 1)]
            for k_old in range(N_e + 1):
                for s_old in range(S_target + 1):
                    if dp[k_old][s_old] == 0:
                        continue

                    # Number of d_val chosen for multiset_E
                    for e_d in range(C_d + 1):
                        k_new = k_old + e_d
                        s_new = s_old + (e_d * d_val)

                        if k_new <= N_e and s_new <= S_target:
                            term_for_d = nCr_mod(C_d, e_d)
                            contribution = (dp[k_old][s_old] * term_for_d) % MOD
                            new_dp[k_new][s_new] = (new_dp[k_new][s_new] + contribution) % MOD

            dp = new_dp

        sum_prod_binom_coeffs = dp[N_e][S_target]

        if sum_prod_binom_coeffs == 0:
            return 0

        # Calculate constant factor F = (N_e! * N_o!) / (C_0! * C_1! * ... * C_9!)
        factor_numerator = (fact[N_e] * fact[N_o]) % MOD

        factor_denominator_inv = 1
        for d_val_iter in range(10):
            factor_denominator_inv = (factor_denominator_inv * invfact[original_counts[d_val_iter]]) % MOD

        constant_factor_F = (factor_numerator * factor_denominator_inv) % MOD

        final_ans = (constant_factor_F * sum_prod_binom_coeffs) % MOD

        return final_ans