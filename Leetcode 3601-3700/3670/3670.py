# Leetcode 3670: Maximum Product of Two Integers With No Common Bits
# https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/
# Solved on 1st of December, 2025
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Calculates the maximum product of two integers from the given list such that
        their binary representations have no common set bits.

        Args:
            nums: A list of non-negative integers.
        Returns:
            The maximum product of two integers with no common bits.
        """
        if not nums:
            return 0

        maxVal = max(nums)
        bitLength = maxVal.bit_length()
        capacity = 1 << bitLength
        dp = [0] * capacity

        for num in nums:
            dp[num] = num

        for i in range(bitLength):
            offset = 1 << i
            step = offset * 2
            for base in range(0, capacity, step):
                for j in range(base, base + offset):
                    if dp[j] > dp[j + offset]:
                        dp[j + offset] = dp[j]

        maxResult = 0
        mask = capacity - 1

        for num in nums:
            complement = mask ^ num
            prod = num * dp[complement]
            if prod > maxResult:
                maxResult = prod

        return maxResult