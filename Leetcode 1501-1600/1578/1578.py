# Leetcode 1578: Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Solved on 3rd of November, 2025
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        """
        Calculates the minimum time needed to make the rope colorful such that no two adjacent balloons have the same color.

        Args:
            colors (str): A string representing the colors of the balloons.
            neededTime (list[int]): A list of integers where neededTime[i] is the time (in seconds) needed to remove the i-th balloon.

        Returns:
            int: The minimum time (in seconds) to remove balloons such that no two adjacent balloons have the same color.
        """
        totalTime = 0
        n = len(colors)

        if n == 0:
            return 0

        maxTimeInGroup = neededTime[0]
        sumTimeInGroup = neededTime[0]

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                sumTimeInGroup += neededTime[i]
                maxTimeInGroup = max(maxTimeInGroup, neededTime[i])
            else:
                totalTime += (sumTimeInGroup - maxTimeInGroup)
                sumTimeInGroup = neededTime[i]
                maxTimeInGroup = neededTime[i]

        totalTime += (sumTimeInGroup - maxTimeInGroup)

        return totalTime