# Leetcode 2088: Count Fertile Pyramids in a Land
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
# Solved on 20th of August, 2025
class Solution:
    def countPyramids(self, grid: list[list[int]]) -> int:
        """
        Counts the total number of fertile pyramids (both regular and inverse) in a given grid.

        Args:
            grid (list[list[int]]): A 2D grid where 1 represents fertile land and 0 represents barren land.
        Returns:
            int: The total count of fertile pyramids.
        """
        def calculate(currentGrid: list[list[int]]) -> int:
            rows = len(currentGrid)
            cols = len(currentGrid[0])
            pyramidCount = 0

            # Create a modifiable copy to serve as the DP table
            dp = [row[:] for row in currentGrid]

            # Iterate from the second to last row up to the top
            for r in range((rows - 2), -1, -1):
                # Iterate through interior columns
                for c in range(1, cols - 1):
                    # Check if a pyramid can be formed from this apex
                    if dp[r][c] == 1:
                        height = 1 + min(dp[r + 1][c - 1], dp[r + 1][c], dp[r + 1][c + 1])
                        dp[r][c] = height
                        # A pyramid of height 'h' adds h - 1 valid pyramids (heights 2 to h)
                        pyramidCount += height - 1

            return pyramidCount

        # Count regular downward-pointing pyramids
        regularCount = calculate(grid)

        # Count inverse pyramids by calculating on a reversed grid
        reversedGrid = grid[::-1]
        inverseCount = calculate(reversedGrid)

        return regularCount + inverseCount