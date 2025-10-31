# Leetcode 3281: Maximize Score of Numbers in Ranges
# https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/
# Solved on 30th of October, 2025
class Solution:
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        """
        This function calculates the maximum possible score such that it's possible to assign a value to each interval
        [start_i, end_i] where end_i - start_i >= score and end_i - start_i <= d.

        :param start: A list of integers representing the start points of the intervals.
        :param d: An integer representing the maximum allowed difference between end and start.
        :return: An integer representing the maximum possible score.
        """
        def isScorePossible(score, sortedStarts, dVal):
            numIntervals = len(sortedStarts)
            currentVal = sortedStarts[0]

            for i in range(1, numIntervals):
                nextVal = max(sortedStarts[i], currentVal + score)

                if nextVal > sortedStarts[i] + dVal:
                    return False

                currentVal = nextVal

            return True

        sortedStartList = sorted(start)

        low = 0
        high = 2_000_000_000
        maxScore = 0

        while low <= high:
            midScore = (low + high) // 2

            if isScorePossible(midScore, sortedStartList, d):
                maxScore = midScore
                low = midScore + 1
            else:
                high = midScore - 1

        return maxScore