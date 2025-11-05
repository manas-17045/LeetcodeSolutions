# Leetcode 2731: Movement of Robots
# https://leetcode.com/problems/movement-of-robots/
# Solved on 5th of November, 2025
class Solution:
    def sumDistance(self, nums: list[int], s: str, d: int) -> int:
        """
        Calculates the sum of distances between all pairs of robots after 'd' seconds.

        Args:
            nums: A list of integers representing the initial positions of the robots.
            s: A string representing the initial directions of the robots ('L' for left, 'R' for right).
            d: An integer representing the time in seconds.

        Returns:
            An integer representing the sum of distances between all pairs of robots.
        """

        n = len(nums)
        finalPositions = []
        modVal = 1000000007

        for i in range(n):
            if s[i] == 'L':
                finalPositions.append(nums[i] - d)
            else:
                finalPositions.append(nums[i] + d)

        finalPositions.sort()

        totalDistance = 0
        prefixSum = 0

        for i in range(n):
            currentPos = finalPositions[i]

            distToPrevious = (i * currentPos) - prefixSum

            totalDistance = (totalDistance + distToPrevious) % modVal
            prefixSum = (prefixSum + currentPos) % modVal

        return totalDistance