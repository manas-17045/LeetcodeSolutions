# Leetcode 2134: Minimum Swaps to Group All 1's Together II
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
# Solved on 24th of October, 2025
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of swaps required to group all 1's together in a circular array.

        Args:
            nums (list[int]): A list of integers, where each element is either 0 or 1.

        Returns:
            int: The minimum number of swaps needed to group all 1's.
        """
        n = len(nums)
        totalOnes = sum(nums)

        if totalOnes == 0 or totalOnes == n:
            return 0

        windowSize = totalOnes
        currentZeros = 0

        for i in range(windowSize):
            if nums[i] == 0:
                currentZeros += 1

        minZeros = currentZeros

        for i in range(1, n):
            leavingIndex = i - 1
            enteringIndex = (i + windowSize - 1) % n

            if nums[leavingIndex] == 0:
                currentZeros -= 1

            if nums[enteringIndex] == 0:
                currentZeros += 1

            minZeros = min(minZeros, currentZeros)

        return minZeros