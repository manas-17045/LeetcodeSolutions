# Leetcode 3343: Count Number of Balanced Permutations
# https://leetcode.com/problems/count-number-of-balanced-permutations/
from collections import Counter


class Solution:
    def countBalancedPermutations(self, num_str: str) -> int:
        """
        Counts the number of balanced permutations of a given numerical string. A balanced
        permutation is defined as a permutation of the provided digits that can be split
        into two multisets, with the sum of the elements in both multisets equal.

        :param num_str: Input string consisting of numerical digits for which balanced
                        permutations are to be calculated.
        :return: The total count of balanced permutations modulo 10^9+7.
        """
        MOD = 10 ** 9 + 7
        N = len(num_str)

        # Calculate frequency of each digit and total sum of digits
        # e.g., for each "121", original_counts = {1: 2, 2: 1}
        original_digit_counts = Counter(int(digit_char) for digit_char in num_str)
        total_sum_of_digits = sum(int(digit_char) for digit_char in num_str)

        # If the total sum is odd, it's impossible to split into two equal sum halves
        if total_sum_of_digits % 2 != 0:
            return 0

        target_sum_for_half = total_sum_of_digits // 2

        # N_e: number of elements at even positions (0-indexed: 0, 2, ...)
        # N_o: number of elements at odd positions (0-indexed: 1, 3, ...)
        num_elements_even_indices = (N + 1) // 2
        num_elements_odd_indices = N // 2

        # Precompute factorials and inverse factorials mmodulo MOD
        # fact[i] = i! % MOD
        # inv_fact[i] = (i!)^(-1) % MOD
        fact = [1] * (N + 1)
        inv_fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        # Using Fermat's Little Theorem for modular inverse
        for i in range(N - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

        # Helper function to calculate nCr % MOD (combinations)
        def nCr_mod(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            # nCr = n! / (r! * (n - r)!)
            numerator = fact[n_val]
            denominator = (inv_fact[r_val] * inv_fact[n_val - r_val]) % MOD
            return (numerator * denominator) % MOD

        # Dynamic Programming
        # dp_state[k][s] = Number of ways to choose 'k' digits for the even-indexed positions
        #                  from the digit types processed so far, such that their sum is 's'.
        # "Number of ways" here refers to the sum of products of binomial coefficients:
        # Sum over (choices of e_d for digits processed) [ Product_d (C_d choose e_d) ]
        # where C_d is total count of digit d, e_d is count of digit d chosen for even set.
        dp_state = [[0] * (target_sum_for_half + 1) for _ in range(num_elements_even_indices + 1)]
        # Base case: 0 items sum to 0 in 1 way (empty selection)
        dp_state[0][0] = 1

        # Iterate through each digit type (0 through 9)
        for digit_value in range(10):
            count_of_current_digit = original_digit_counts[digit_value]

            # If this digit is not present in the input number, C_d = 0.
            # The loops for e_d would only run for e_d = 0, nCr(0, 0) = 1,
            # effectively copying dp_state to next_dp_state. So, skipping is an optimization.
            if count_of_current_digit == 0:
                continue

            # next_dp_state incorporates the current digit_value
            next_dp_state = [[0] * (target_sum_for_half + 1) for _ in range(num_elements_even_indices + 1)]

            # k_prev_half: number of items chosen for even half from *previous* digit types
            # s_prev_half: sum of items chosen for even half from *previous* digit types
            for k_prev_half in range(num_elements_even_indices + 1):
                for s_prev_half in range(target_sum_for_half + 1):
                    if dp_state[k_prev_half][s_prev_half] == 0:
                        continue

                    # num_current_digit_for_even_half: count of current digit_value choosen for even-indexed multiset
                    for num_current_digit_for_even_half in range(count_of_current_digit + 1):
                        k_new_half = k_prev_half + num_current_digit_for_even_half
                        s_new_half = s_prev_half + (num_current_digit_for_even_half * digit_value)

                        if k_new_half <= num_elements_even_indices and s_new_half <= target_sum_for_half:
                            # Ways to choose 'num_current_digit_for_even_half' from 'count_of_current_digit' available
                            ways_to_choose_current_digit = nCr_mod(count_of_current_digit, num_current_digit_for_even_half)
                            contribution = (dp_state[k_prev_half][s_prev_half] * ways_to_choose_current_digit) % MOD
                            next_dp_state[k_new_half][s_new_half] = (next_dp_state[k_new_half][s_new_half] + contribution) % MOD

            # Update dp_state table for the next digit type
            dp_state = next_dp_state

        # sum_of_products_of_binomials = dp_state[num_elements_even_indices][target_sum_for_half]
        # This is Sum[ Product_d[ nCr(C_d, e_d) ] ] over all valid distributions {e_d}
        # such that Sum[e_d] = num_elements_even_indices and Sum[e_d * d] = target_sum_for_half.
        sum_of_products_of_binomials = dp_state[num_elements_even_indices][target_sum_for_half]

        if sum_of_products_of_binomials == 0:
            # No way to partition the digits to satisfy the conditions
            return 0

        # Combinatorial Factor Calculation:
        # The DP result (sum_of_products_of_binomials) gives the number of ways to assign
        # the original items (considering identical items) to the even-indexed set.
        # To get the number of distinct permutations, we multiply by a factor:
        # Factor = (num_elements_even_indices! * num_elements_odd_indices!) / (C_0! * C_1! * ... * C_9!)
        # The final answer is sum_of_products_of_binomials * Factor.
        # This is equivalent to Sum over partitions {e_d}, {o_d} of:
        #   (num_elements_even_indices! / Product[e_d!]) * (num_elements_odd_indices! / Product[o_d!])
        # where e_d is count of digit d in even set, o_d is count of digit d in odd set.
        factor_numerator = (fact[num_elements_even_indices] * fact[num_elements_odd_indices]) % MOD

        factor_denominator_inv = 1
        # Iterate through all digit types 0-9
        for i in range(10):
            # original_digit_counts[i] will be 0 if digit i is not in num_str.
            # inv_fact[0] is 1.
            factor_denominator_inv = (factor_denominator_inv * inv_fact[original_digit_counts[i]]) % MOD

        final_combinatorial_factor = (factor_numerator * factor_denominator_inv) % MOD

        total_balanced_permutations = (final_combinatorial_factor * sum_of_products_of_binomials) % MOD

        return total_balanced_permutations