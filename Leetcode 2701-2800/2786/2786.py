# Leetcode 2786: Visit Array Positions to Maximize Score
# https://leetcode.com/problems/visit-array-positions-to-maximize-score/
# Solved on 24th of November, 2025
class Solution:
    def maxScore(self, nums: list[int], x: int) -> int:
        """
        Calculates the maximum score achievable by visiting array positions.

        Args:
            nums: A list of integers representing the values at each position.
            x: An integer representing the penalty for switching parity.

        Returns:
            The maximum score achievable.
        """
        maxEven = nums[0]
        maxOdd = nums[0]

        if nums[0] % 2 == 0:
            maxOdd -= x
        else:
            maxEven -= x

        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                maxEven = max(maxEven, maxOdd - x) + nums[i]
            else:
                maxOdd = max(maxOdd, maxEven - x) + nums[i]

        return max(maxEven, maxOdd)