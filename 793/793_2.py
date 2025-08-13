# Leetcode 793: Preimage Size of Factorial Zeroes Function
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# Solved on 13th of August, 2025
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """
        Calculates the number of non-negative integers x such that the number of trailing zeros in x! is equal to k.
        :param k: An integer representing the target number of trailing zeros.
        :return: The count of non-negative integers x whose factorial has exactly k trailing zeros.
        """
        def trailingZeros(x: int) -> int:
            cnt = 0
            while x:
                x //= 5
                cnt += x
            return cnt

        def firstWithAtLeast(target: int) -> int:
            lo, hi = 0, 5 * (target + 1)
            while lo < hi:
                mid = (lo + hi) // 2
                if trailingZeros(mid) >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        return firstWithAtLeast(k + 1) - firstWithAtLeast(k)