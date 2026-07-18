# Leetcode 3975: Filter Occupied Intervals
# https://leetcode.com/problems/filter-occupied-intervals/
# Solved on 18th of July, 2026
class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: list[list[int]], freeStart: int, freeEnd: int) -> list[list[int]]:
        """
        Filters occupied intervals to remove those within the free time range.

        Args:
            occupiedIntervals: The occupied time intervals.
            freeStart: The start of the free time range.
            freeEnd: The end of the free time range.

        Returns:
            The filtered list of occupied intervals.
        """
        if not occupiedIntervals:
            return []

        occupiedIntervals.sort(key=lambda interval: interval[0])

        mergedIntervals = []
        currentStart, currentEnd = occupiedIntervals[0]

        for i in range(1, len(occupiedIntervals)):
            nextStart, nextEnd = occupiedIntervals[i]
            if nextStart <= currentEnd + 1:
                currentEnd = max(currentEnd, nextEnd)
            else:
                mergedIntervals.append([currentStart, currentEnd])
                currentStart, currentEnd = nextStart, nextEnd

        mergedIntervals.append([currentStart, currentEnd])

        resultIntervals = []
        for startInterval, endInterval in mergedIntervals:
            if startInterval > freeEnd or endInterval < freeStart:
                resultIntervals.append([startInterval, endInterval])
            else:
                if startInterval < freeStart:
                    resultIntervals.append([startInterval, freeStart - 1])
                if endInterval > freeEnd:
                    resultIntervals.append([freeEnd + 1, endInterval])

        return resultIntervals