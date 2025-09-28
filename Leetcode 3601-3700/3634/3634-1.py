# Leetcode 3634: Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/
# Solved on 28th of September, 2025
import bisect


class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of removals to balance the array.

        Args:
            nums: A list of integers.
            k: An integer representing the balancing factor.

        Returns:
            The minimum number of removals required to balance the array.
        """

        listSize = len(nums)
        if listSize <= 1:
            return 0

        nums.sort()

        maxLength = 1

        for i in range(listSize):
            minVal = nums[i]
            maxAllowedVal = minVal * k

            rightBoundary = bisect.bisect_right(nums, maxAllowedVal)

            currentLength = rightBoundary - i

            if currentLength > maxLength:
                maxLength = currentLength

        return listSize - maxLength