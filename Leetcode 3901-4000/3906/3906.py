# Leetcode 3906: Count Good Integers on a Grid Path
# https://leetcode.com/problems/count-good-integers-on-a-grid-path/
# Solved on 2nd of May, 2026
class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        """
        Counts the number of integers in the range [l, r] such that the digits
        at positions corresponding to a path on a 4x4 grid are non-decreasing.

        :param l: The lower bound of the range (inclusive).
        :param r: The upper bound of the range (inclusive).
        :param directions: A string of 'D' and 'R' representing the path on a 4x4 grid.
        :return: The total count of good integers within the specified range.
        """
        pathIndices = set()
        currRow = 0
        currCol = 0
        pathIndices.add(0)

        for directionChar in directions:
            if directionChar == 'D':
                currRow += 1
            else:
                currCol += 1
            pathIndices.add(currRow * 4 + currCol)

        def countValid(upperBound: int) -> int:

            if upperBound < 0:
                return 0

            numStr = str(upperBound).zfill(16)
            memo = {}

            def dfs(pos: int, isTight: bool, lastVal: int) -> int:

                if pos == 16:
                    return 1

                state = (pos, isTight, lastVal)
                if state in memo:
                    return memo[state]

                maxDigit = int(numStr[pos]) if isTight else 9
                totalWays = 0
                isPathPos = pos in pathIndices

                for currentDigit in range(maxDigit + 1):
                    if isPathPos and currentDigit < lastVal:
                        continue

                    nextTight = isTight and (currentDigit == maxDigit)
                    nextLastVal = currentDigit if isPathPos else lastVal

                    totalWays += dfs(pos + 1, nextTight, nextLastVal)

                memo[state] = totalWays
                return totalWays

            return dfs(0, True, 0)

        return countValid(r) - countValid(l - 1)