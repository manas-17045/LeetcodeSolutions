# Leetcode 1611: Minimum One Bit Operations to Make Integers Zero
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
# Solved on 17th of July, 2025
from functools import lru_cache


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        This problem can be solved by observing a pattern related to Gray codes.
        The operation is essentially converting a number to 0 using a specific set of rules.
        The key insight is that the number of operations to convert `x` to `0` is related to
        the number of operations to convert `x - 2^k` to `0`, where `2^k` is the largest power of 2 less than or equal to `x`.
        This leads to a recursive formula.
        """
        @lru_cache(None)
        def f(x: int) -> int:
            if x == 0:
                return 0
            # k = index of highest set bit in x
            k = x.bit_length() - 1
            # Reflect around 2^k
            return (1 << (k + 1)) - 1 - f(x - (1 << k))

        # Clear cache
        f.cache_clear()
        return f(n)