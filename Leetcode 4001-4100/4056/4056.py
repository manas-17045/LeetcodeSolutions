# Leetcode 4056: Numnber of Intersecting Interval Pairs I
# https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/
# Solved on 23rd of October, 2026
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        """
        Calculates the number of pairs of intervals that intersect.

        Parameters:
            intervals (list[list[int]]): A list of closed intervals where each element is [start, end].

        Returns:
            int: The total count of intersecting pairs (i, j) with 0 <= i < j < len(intervals).
        """
        totalCount = len(intervals)
        totalPairs = totalCount * (totalCount - 1) // 2
        startTimes = sorted(singleInterval[0] for singleInterval in intervals)
        endTimes = sorted(singleInterval[1] for singleInterval in intervals)

        disjointPairs = 0
        endPointer = 0

        for currentStart in startTimes:
            while endPointer < totalCount and endTimes[endPointer] < currentStart:
                endPointer += 1
            disjointPairs += endPointer

        return totalPairs - disjointPairs