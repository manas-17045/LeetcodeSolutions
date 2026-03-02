# Leetcode 3858: Minimum Bitwise OR From Grid
# https://leetcode.com/problems/minimum-bitwise-or-from-grid/
# Solved on 2nd of March, 2026
class Solution:
    def minimumOR(self, grid: list[list[int]]) -> int:
        """
        Finds the minimum bitwise OR sum possible by picking one element from each row.

        :param grid: A 2D list of integers representing the grid.
        :return: The minimum possible bitwise OR value of a selection containing one element per row.
        """
        targetMask = (1 << 17) - 1
        for bitIndex in range(16, -1, -1):
            testMask = targetMask ^ (1 << bitIndex)

            isPossible = True
            for gridRow in grid:
                hasValidNumber = False

                for cellValue in gridRow:
                    if (cellValue | testMask) == testMask:
                        hasValidNumber = True
                        break

                if not hasValidNumber:
                    isPossible = False
                    break

            if isPossible:
                targetMask = testMask

        return targetMask