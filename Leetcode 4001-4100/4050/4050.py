# Leetcode 4050: Minimum Days to Score Exactly N Points
# https://leetcode.com/problems/minimum-days-to-score-exactly-n-points/
# Solved on 13th of October, 2026
class Solution:
    def minDays(self, n: int) -> int:
        """
        Calculate the minimum number of days required to reach exactly n points.

        Parameters:
            n (int): The target score to reach.

        Returns:
            int: The minimum total days needed to reach the score.
        """
        minDays = [i * 2 for i in range(n + 1)]
        streakLength = 2

        while True:
            points = streakLength * (streakLength + 1) // 2
            if points > n:
                break

            dayCost = streakLength + 1
            for score in range(points, n + 1):
                if minDays[score - points] + dayCost < minDays[score]:
                    minDays[score] = minDays[score - points] + dayCost

            streakLength += 1

        return minDays[n] - 1