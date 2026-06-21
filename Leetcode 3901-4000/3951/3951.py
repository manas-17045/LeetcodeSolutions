# Leetcode 3951: Minimum Energy to Maintain Brightness
# https://leetcode.com/problems/minimum-energy-to-maintain-brightness/
# Solved on 21st of June, 2026
class Solution:
    def minEnergy(start, n: int, brightness: int, intervals: list[list[int]]) -> int:
        """
        Calculates the minimum energy required to maintain the brightness level.
        
        :param start: The starting position.
        :param n: The total number of positions.
        :param brightness: The brightness level to maintain.
        :param intervals: A list of intervals where brightness is required.
        :return: The minimum energy required.
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        totalTime = 0
        currStart, currEnd = intervals[0][0], intervals[0][1]
        for intervalStart, intervalEnd in intervals[1:]:
            if intervalStart <= currEnd:
                currEnd = max(currEnd, intervalEnd)
            else:
                totalTime += (currEnd - currStart + 1)
                currStart, currEnd = intervalStart, intervalEnd
        
        totalTime += (currEnd - currStart + 1)
        minBulbs = (brightness + 2) // 3
        return minBulbs * totalTime