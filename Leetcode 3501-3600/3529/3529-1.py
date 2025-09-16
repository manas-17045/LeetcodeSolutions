# Leetcode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/
# Solved on 16th of September, 2025
class Solution:
    def countCells(self, grid: list[list[int]], pattern: str) -> int:
        """
        Counts the number of cells that are part of both a horizontal and a vertical occurrence of the given pattern.
        :param grid: A 2D list of integers representing the grid.
        :param pattern: A string representing the pattern to search for.
        :return: The total count of cells that are covered by both a horizontal and a vertical pattern match.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        patternLen = len(pattern)

        def computeLPS(pat: str) -> list[int]:
            patLen = len(pat)
            lps = [0] * patLen
            length = 0
            i = 1
            while i < patLen:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def findPatternStarts(text: str, pat: str, lps: list[int]) -> list[int]:
            textLen = len(text)
            patLen = len(pat)
            starts = []
            i = 0
            j = 0
            while i < textLen:
                if pat[j] == text[i]:
                    i += 1
                    j += 1

                if j == patLen:
                    starts.append(i - j)
                    j = lps[j - 1]
                elif i < textLen and pat[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return starts

        def getCoverage(text: str) -> list[bool]:
            textLen = len(text)
            if patternLen > textLen:
                return [False] * textLen

            lps = computeLPS(pattern)
            starts = findPatternStarts(text, pattern, lps)

            coverage = [False] * textLen
            if not starts:
                return coverage

            diff = [0] * (textLen + 1)
            for startIndex in starts:
                diff[startIndex] += 1
                endIndex = startIndex + patternLen
                if endIndex <= textLen:
                    diff[endIndex] -= 1

            activeMatches = 0
            for i in range(textLen):
                activeMatches += diff[i]
                if activeMatches > 0:
                    coverage[i] = True
            return coverage

        flatGridHorizontal = "".join("".join(row) for row in grid)
        horizontalCoverage = getCoverage(flatGridHorizontal)

        flatGridVertical = "".join(grid[r][c] for c in range(numCols) for r in range(numRows))
        verticalCoverage = getCoverage(flatGridVertical)

        overlapCount = 0
        for r in range(numRows):
            for c in range(numCols):
                hIndex = r * numCols + c
                vIndex = c * numRows + r
                if horizontalCoverage[hIndex] and verticalCoverage[vIndex]:
                    overlapCount += 1

        return overlapCount