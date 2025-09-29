# Leetcode 3022: Minimize OR of Remaining Elements Using Operations
# https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/
# Solved on 29th of September, 2025
class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        """
        This function aims to minimize the bitwise OR of the remaining elements after performing at most k operations.
        An operation consists of splitting the array into two non-empty subarrays.
        :param nums: A list of integers.
        :param k: The maximum number of operations allowed.
        :return: The minimum possible bitwise OR of the remaining elements.
        """
        def isFeasible(targetValue: int) -> bool:

            groups = 0
            currentAnd = -1

            for num in nums:
                currentAnd &= num
                if (currentAnd | targetValue) == targetValue:
                    groups += 1
                    currentAnd = -1

            operationsNeeded = len(nums) - groups
            return operationsNeeded <= k

        ans = 0
        for b in range(29, -1, -1):
            potentialBit = 1 << b

            testTarget = ans | potentialBit

            if isFeasible(testTarget):
                ans |= potentialBit


        ans = 0
        for b in range(29, -1, -1):
            potentialBit = 1 << b

            testTarget = ans | (potentialBit - 1)

            if not isFeasible(testTarget):
                ans |= potentialBit

        return ans