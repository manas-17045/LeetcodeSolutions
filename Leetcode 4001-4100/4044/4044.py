# Leetcode 4044: Count Good Cyclic Rotations
# https://leetcode.com/problems/count-good-cyclic-rotations/
# Solved on 6th of October, 2026
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        """
        Calculates the number of cyclic rotations where the sum of the first
        half of the elements strictly exceeds the sum of the remaining half.

        Parameters:
            nums (list[int]): An even-length list of positive integers.

        Returns:
            int: Total number of valid cyclic rotations.
        """
        totalLen = len(nums)
        halfLen = totalLen // 2
        totalSum = sum(nums)
        windowSum = sum(nums[currIdx] for currIdx in range(halfLen))
        goodRotations = 0

        for startIndex in range(totalLen):
            if 2 * windowSum > totalSum:
                goodRotations += 1

            windowSum += nums[(startIndex + halfLen) % totalLen] - nums[startIndex]

        return goodRotations