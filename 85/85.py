# Leetcode 85: Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/
# Solved on 11th of January, 2026
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        """
        Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle
        containing only 1's and return its area.

        This problem can be reduced to the "Largest Rectangle in Histogram" problem.
        For each row, we calculate the heights of consecutive '1's above it.
        Then, we apply the largest rectangle in histogram algorithm to find the maximum area for that row.
        The overall maximum area is the answer.

        Args:
            matrix (list[list[str]]): A 2D binary matrix where each element is '0' or '1'.
        Returns:
            int: The area of the largest rectangle containing only '1's.
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = [-1]
            for j in range(cols + 1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[j]:
                    currentHeight = heights[stack.pop()]
                    currentWidth = j - stack[-1] - 1
                    maxArea = max(maxArea, currentHeight * currentWidth)

                stack.append(j)

        return maxArea