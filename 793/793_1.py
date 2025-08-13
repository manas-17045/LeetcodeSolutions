# Leetcode 793: Preimage Size of Factorial Zeroes Function
# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# Solved on 13th of August, 2025
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """
        Given an integer k, return the number of non-negative integers x such that factorial(x) has exactly k trailing zeros.

        :param k: The target number of trailing zeros.
        :return: The number of non-negative integers x such that x! has exactly k trailing zeros.
        """
        def countTrailingZeros(n: int) -> int:
            count = 0
            powerOfFive = 5
            while powerOfFive <= n:
                count += n // powerOfFive
                if powerOfFive > n / 5:
                    break
                powerOfFive *= 5
            return count

        low = 0
        high = 5 * (k + 1)

        while low <= high:
            mid = low + (high - low) // 2
            zerosCount = countTrailingZeros(mid)

            if zerosCount < k:
                low = mid + 1
            else:
                high = mid - 1

        if countTrailingZeros(low) == k:
            return 5
        else:
            return 0