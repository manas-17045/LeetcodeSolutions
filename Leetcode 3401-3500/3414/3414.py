# Leetcode 3414: Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
# Solved on 1st of November, 2025
import bisect


class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        """
        Calculates the maximum score of non-overlapping intervals.

        Args:
            intervals: A list of intervals, where each interval is [start, end, weight].
        Returns:
            A list of original indices of the selected intervals that yield the maximum score.
        """
        def compareStates(stateA, stateB):
            scoreA, indicesA = stateA
            scoreB, indicesB = stateB

            if scoreA > scoreB:
                return stateA
            if scoreB > scoreA:
                return stateB

            if indicesA < indicesB:
                return stateA
            else:
                return stateB

        n = len(intervals)

        indexedIntervals = []
        for i in range(n):
            indexedIntervals.append((intervals[i][0], intervals[i][1], intervals[i][2], i))

        sortedIntervals = sorted(indexedIntervals, key=lambda x: x[1])

        endTimes = [interval[1] for interval in sortedIntervals]

        dp = []
        for _ in range(n + 1):
            dp.append([(0, []) for _ in range(5)])

        for k in range(1, 5):
            for i in range(1, n + 1):
                start, end, weight, originalIndex = sortedIntervals[i - 1]

                optionOne = dp[i - 1][k]

                insertionPoint = bisect.bisect_left(endTimes, start)

                prevScore, prevIndices = dp[insertionPoint][k - 1]

                newScore = prevScore + weight

                newIndicesList = prevIndices + [originalIndex]
                newIndicesList.sort()

                optionTwo = (newScore, newIndicesList)

                dp[i][k] = compareStates(optionOne, optionTwo)

        bestSolution = (0, [])
        for k in range(1, 5):
            bestSolution = compareStates(bestSolution, dp[n][k])

        return bestSolution[1]