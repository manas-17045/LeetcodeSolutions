# Leetcode 3490: Count Beautiful Numbers
# https://leetcode.com/problems/count-beautiful-numbers/
# Solved on 4th of October, 2025
from collections import defaultdict
from functools import lru_cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        """
        Calculates the number of "beautiful numbers" within a given range [l, r].
        A number is beautiful if the product of its digits is divisible by the sum of its digits.
        :param l: The lower bound of the range (inclusive).
        :param r: The upper bound of the range (inclusive).
        :return: The count of beautiful numbers in the range [l, r].
        """
        def count_upto(N: int) -> int:
            if N <= 0:
                return 0
            digits = list(map(int, str(N)))
            n = len(digits)
            max_sum = 9 * n

            # caps for prime exponents needed for sums up to max_sum
            def cap_for(p):
                cap = 0
                v = 1
                while v * p <= max_sum:
                    v *= p
                    cap += 1
                return cap

            cap2 = cap_for(2)
            cap3 = cap_for(3)
            cap5 = cap_for(5)
            cap7 = cap_for(7)

            # precompute factorization requirements for each sum s in [1..max_sum]
            req = [None] * (max_sum + 1)
            possible = [False] * (max_sum + 1)
            for s in range(1, max_sum + 1):
                x = s
                e2 = e3 = e5 = e7 = 0
                while x % 2 == 0:
                    e2 += 1;
                    x //= 2
                while x % 3 == 0:
                    e3 += 1;
                    x //= 3
                while x % 5 == 0:
                    e5 += 1;
                    x //= 5
                while x % 7 == 0:
                    e7 += 1;
                    x //= 7
                if x == 1:
                    possible[s] = True
                    req[s] = (min(e2, cap2), min(e3, cap3), min(e5, cap5), min(e7, cap7))
                else:
                    possible[s] = False
                    req[s] = (0, 0, 0, 0)

            # prime-exponent increments for digits 0..9
            digit_inc = {
                0: (0, 0, 0, 0),
                1: (0, 0, 0, 0),
                2: (1, 0, 0, 0),
                3: (0, 1, 0, 0),
                4: (2, 0, 0, 0),
                5: (0, 0, 1, 0),
                6: (1, 1, 0, 0),
                7: (0, 0, 0, 1),
                8: (3, 0, 0, 0),
                9: (0, 2, 0, 0),
            }

            @lru_cache(maxsize=None)
            def dp(pos: int, tight: bool, started: bool):
                """
                Return a dict mapping:
                  (has_zero_flag, sum_of_digits, e2, e3, e5, e7) -> count
                for all numbers that can be formed from digits[pos:]
                given whether we already 'started' (a non-leading non-zero appeared to the left).
                """
                if pos == n:
                    # empty suffix: one way (no digits added)
                    return {(0, 0, 0, 0, 0, 0): 1}

                limit = digits[pos] if tight else 9
                res = defaultdict(int)

                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    new_started = started or (d != 0)
                    child = dp(pos + 1, ntight, new_started)
                    inc = digit_inc[d]

                    for (child_has_zero, child_sum, ce2, ce3, ce5, ce7), cnt in child.items():
                        total_sum = child_sum + d  # adding current digit (0 adds 0)
                        # A zero at current position only makes product zero if there was some non-zero to its left:
                        has_zero = child_has_zero or (started and d == 0)
                        if has_zero:
                            # canonicalize exponents to zeros to collapse states
                            key = (1, total_sum, 0, 0, 0, 0)
                            res[key] += cnt
                        else:
                            # combine exponents (cap them)
                            ne2 = min(ce2 + inc[0], cap2)
                            ne3 = min(ce3 + inc[1], cap3)
                            ne5 = min(ce5 + inc[2], cap5)
                            ne7 = min(ce7 + inc[3], cap7)
                            key = (0, total_sum, ne2, ne3, ne5, ne7)
                            res[key] += cnt
                return dict(res)

            mapping = dp(0, True, False)

            total = 0
            for (has_zero, ssum, e2, e3, e5, e7), cnt in mapping.items():
                if ssum == 0:
                    # zero (all digits zero) or no started -> skip (problem considers positive integers)
                    continue
                if has_zero:
                    # product is zero => divisible by any positive sum
                    total += cnt
                else:
                    if not possible[ssum]:
                        continue
                    re2, re3, re5, re7 = req[ssum]
                    if e2 >= re2 and e3 >= re3 and e5 >= re5 and e7 >= re7:
                        total += cnt

            return total

        return count_upto(r) - count_upto(l - 1)