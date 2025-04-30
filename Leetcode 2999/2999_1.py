# Leetcode 2999: Count the Number of Powerful Integers
# https://leetcode.com/problems/count-the-number-of-powerful-integers/
from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        Calculate the count of "powerful integers" between a specified range which end in a
        given substring `s` and adhere to specific digit constraints.

        A "powerful integer" is defined as an integer that ends with the specified substring
        `s`, and all its digits do not exceed a given limit.

        :param start: The starting point of the range (inclusive)
        :type start: int
        :param finish: The end point of the range (inclusive)
        :type finish: int
        :param limit: The maximum allowed value for any digit in the integers
        :type limit: int
        :param s: A string representation of the fixed ending substring
        :type s: str
        :return: The count of integers in the range [start, finish] that satisfy the
            defined conditions
        :rtype: int
        """
        s_val_str = s

        try:
            # Ensure s represents a positive integer as per constraints
            s_val = int(s_val_str)
            if s_val == 0:
                return 0
        except ValueError:
            # s should always be a valid integer string based on constraints
            return 0

        len_s = len(s_val_str)
        power_of_10 = 10**len_s

        # --- Pre-check: Digits in s must respect the limit ---
        if any(int(digit) > limit for digit in s_val_str):
            return 0    # Impossible to form such a number

        # --- Helper function to count powerful integers <= N ---
        def solve(N_long: int) -> int:

            # Handle edge case for count(start - 1) where start might be 1
            if N_long < 0:
                return 0

            # If N is less than s itself, no number <= N can end in s
            if s_val > N_long:
                return 0

            # Calculate the maximum possible prefix such that
            # prefix * (10^len_s) + s_val <= N_long
            max_prefix = (N_long - s_val) // power_of_10
            P_str = str(max_prefix)
            n_p = len(P_str)

            # Digit DP function to count integers p in [0, max_prefix]
            # such that all digits of p are <= limit
            @cache
            def dp(index: int, is_less: bool, is_leading_zero: bool) -> int:
                # Base case: Reached the end of the orefix number
                if index == n_p:
                    # We successfully formed a prefix of length n_p (could be 0 if P=0)
                    return 1

                res = 0
                # Determine the upper bound for the current digit
                # If is_less is True, we can use any digit up to limit.
                # Otherwise, we are restricted by the digit in P_str at this index.
                upper_bound_p = int(P_str[index]) if not is_less else 9

                # Iterate through possible digits for the current position
                for digit in range(min(upper_bound_p, limit) + 1):
                    # The digit must be <= limit (guaranteed by loop range)
                    # The digit must be <= upper_bound_p (guaranteed by loop range)

                    # Handle leading zeroes separately to count correctly
                    if is_leading_zero and digit == 0:

                        # If we place 0 and P_str[index] is also 0, is_less doesn't change.
                        # If we place 0 and P_str[index] > 0, number becomes strictly less.
                        res += dp(index + 1, is_less or (digit < upper_bound_p), True)
                    else:
                        # Placing a non-zero digit, or placing zero when not leading.
                        # is_leading_zero becomes False.
                        # is_less becomes True if it was already True or if current digit < upper_bound_p.
                        res += dp(index + 1, is_less or (digit < upper_bound_p), False)

                return res

            # Call the DP function to count valid prefixes [0, max_prefix]
            # Start at index 0, is_less is False, is_leadinh_zero is True
            count_prefixes = dp(0, False, True)

            # Clear cache for later calls if solve is called multiple times
            dp.cache_clear()

            return count_prefixes

        # Calculate the final answer using the range counting technique
        ans_finish = solve(finish)
        ans_start_minus_1 = solve(start - 1)

        return ans_finish - ans_start_minus_1