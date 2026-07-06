# Leetcode 1288: Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/
# Solved on 6th of July, 2026
class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        """
        Removes covered intervals from a list of intervals and returns the number of
        remaining intervals.

        Args:
            intervals: The list of intervals.

        Returns:
            The number of remaining intervals.
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remainingCount = 0
        maxRight = 0
        
        for interval in intervals:
            if interval[1] > maxRight:
                remainingCount += 1
                maxRight = interval[1]
                
        return remainingCount