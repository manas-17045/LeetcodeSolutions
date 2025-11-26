# Leetcode 3661: Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/
# Solved on 25th of November, 2025
import bisect


class Solution:
    def maxWalls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:
        """
        Calculates the maximum number of walls that can be destroyed by a sequence of robots.

        Args:
            robots: A list of integers representing the positions of the robots.
            distance: A list of integers representing the destruction range of each robot.
            walls: A list of integers representing the positions of the walls.

        Returns:
            An integer representing the maximum number of walls destroyed.
        """
        combinedRobots = sorted(zip(robots, distance))
        n = len(combinedRobots)

        if n == 0:
            return 0

        robotPositions = set(robots)
        validWalls = []
        alwaysDestroyed = 0

        for w in walls:
            if w in robotPositions:
                alwaysDestroyed += 1
            else:
                validWalls.append(w)

        validWalls.sort()

        def countWalls(low, high):
            if low > high:
                return 0
            leftIdx = bisect.bisect_left(validWalls, low)
            rightIdx = bisect.bisect_right(validWalls, high)
            return max(0, rightIdx - leftIdx)

        p0, d0 = combinedRobots[0]

        prevLeft = countWalls(p0 - d0, p0)

        limitRight = combinedRobots[1][0] if n > 1 else float('inf')
        prevRightRangeLow = p0
        prevRightRangeHigh = min(p0 + d0, limitRight)
        prevRight = countWalls(prevRightRangeLow, prevRightRangeHigh)

        for i in range(1, n):
            pCurr, dCurr = combinedRobots[i]
            pPrev, dPrev = combinedRobots[i - 1]
            pNext = combinedRobots[i + 1][0] if i < n - 1 else float('inf')

            currLeftLow = max(pCurr - dCurr, pPrev)
            currLeftHigh = pCurr
            cntCurrLeft = countWalls(currLeftLow, currLeftHigh)

            valFromLeft = prevLeft + cntCurrLeft

            overlapLow = max(prevRightRangeLow, currLeftLow)
            overlapHigh = min(prevRightRangeHigh, currLeftHigh)
            overlapCount = countWalls(overlapLow, overlapHigh)

            valFromRight = prevRight + cntCurrLeft - overlapCount

            currDpLeft = max(valFromLeft, valFromRight)

            currRightLow = pCurr
            currRightHigh = min(pCurr + dCurr, pNext)
            cntCurrRight = countWalls(currRightLow, currRightHigh)

            currDpRight = max(prevLeft, prevRight) + cntCurrRight

            prevLeft = currDpLeft
            prevRight = currDpRight
            prevRightRangeLow = currRightLow
            prevRightRangeHigh = currRightHigh

        return max(prevLeft, prevRight) + alwaysDestroyed