# Leetcode 3096: Minimum Levels to Gain More Points
# https://leetcode.com/problems/minimum-levels-to-gain-more-points/
# Solved on 4th of January, 2026
class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        """
        Calculates the minimum number of levels Alice needs to complete to have a strictly greater score than Bob.

        :param possible: A list of integers where 1 represents a successful level and 0 represents a failed level.
        :return: The minimum number of levels Alice needs to complete, or -1 if she can never achieve a strictly greater score.
        """
        totalScore = 0
        for p in possible:
            if p == 1:
                totalScore += 1
            else:
                totalScore -= 1

        aliceScore = 0
        n = len(possible)

        for i in range(n - 1):
            if possible[i] == 1:
                aliceScore += 1
            else:
                aliceScore -= 1

            bobScore = totalScore - aliceScore
            if aliceScore > bobScore:
                return i + 1

        return -1