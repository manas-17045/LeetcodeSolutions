# Leetcode 3007: Maximum Number That Sum of the Prices Is Less Than or Equal to K
# https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
# Solved on 7th of October, 2025
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        """
        Finds the maximum number such that the sum of prices is less than or equal to k.

        Args:
            k (int): The maximum allowed sum of prices.
            x (int): The value used to determine the price of set bits.
        Returns:
            int: The maximum number satisfying the condition.
        """
        def countSetBits(n: int, p: int) -> int:
            cycleLen = 1 << (p + 1)
            bitValue = 1 << p

            numCycles = (n + 1) // cycleLen
            count = numCycles * bitValue

            remainder = (n + 1) % cycleLen
            count += max(0, remainder - numCycles)
            return count

        def getAccumulatedPrice(num: int, xVal: int) -> int:
            totalPrice = 0
            bitIndex = xVal - 1
            while bitIndex < 62:
                totalPrice += countSetBits(num, bitIndex)
                bitIndex += xVal
            return totalPrice

        low = 1
        high = 2 * (10**18)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                break

            currentPrice = getAccumulatedPrice(mid, x)

            if currentPrice <= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans