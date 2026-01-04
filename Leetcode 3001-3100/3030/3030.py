# Leetcode 3030: Find the Grid of Region Average
# https://leetcode.com/problems/find-the-grid-of-region-average/
# Solved on 4th of January, 2026
class Solution:
    def resultGrid(self, image: list[list[int]], threshold: int) -> list[list[int]]:
        """
        Calculates the resulting grid where each cell is the average of its 3x3 region if it's a valid region,
        otherwise, it retains its original value.
        :param image: The input 2D grid of integers.
        :param threshold: The maximum allowed difference between adjacent cells in a valid region.
        :return: The modified 2D grid.
        """
        m = len(image)
        n = len(image[0])
        regionSums = [[0] * n for _ in range(m)]
        regionCounts = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                isValid = True
                for r in range(i, i + 3):
                    for c in range(j, j + 2):
                        if abs(image[r][c] - image[r][c + 1]) > threshold:
                            isValid = False
                            break
                    if not isValid:
                        break

                if isValid:
                    for c in range(j, j + 3):
                        for r in range(i, i + 2):
                            if abs(image[r][c] - image[r + 1][c]) > threshold:
                                isValid = False
                                break
                        if not isValid:
                            break

                if isValid:
                    subGridSum = 0
                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            subGridSum += image[r][c]

                    average = subGridSum // 9

                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            regionSums[r][c] += average
                            regionCounts[r][c] += 1

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if regionCounts[i][j] == 0:
                    result[i][j] = image[i][j]
                else:
                    result[i][j] = regionSums[i][j] // regionCounts[i][j]

        return result