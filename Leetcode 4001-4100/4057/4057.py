# Leetcode 4057: Number of Intersecting Interval Pairs II
# https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii/
# Solved on 24th of October, 2026
from bisect import bisect_right


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        """
        Calculates the total number of intersecting pairs of intervals.

        Parameters:
            intervals (list[list[int]]): A list of closed intervals where each interval is represented as [start, end].

        Returns:
            int: The total count of intersecting interval pairs (i, j) such that 0 <= i < j < n.
        """
        sortedIntervals = sorted(intervals, key=lambda intervalItem: intervalItem[0])
        startTimes = [intervalItem[0] for intervalItem in sortedIntervals]
        totalPairs = 0
        totalCount = len(sortedIntervals)

        for currentIndex in range(totalCount):
            endPoint = sortedIntervals[currentIndex][1]
            targetIndex = bisect_right(startTimes, endPoint)
            totalPairs += targetIndex - 1 - currentIndex

        return totalPairs