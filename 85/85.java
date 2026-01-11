// Leetcode 85: Maximal Rectangles
// https://leetcode.com/problems/maximal-rectangle/
// Solved on 11th of January, 2026
class Soluyion {
    /**
     * Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
     *
     * @param matrix The input binary matrix.
     * @return The area of the largest rectangle containing only 1's.
     */
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) {
            return 0;
        }
        int cols = matrix[0].length;
        int[] heights = new int[cols + 1];
        int[] stack = new int[cols + 2];
        int maxArea = 0;

        for (char[] row : matrix) {
            for (int i = 0; i < cols; i++) {
                heights[i] = (row[i] == '1') ? heights[i] + 1 : 0;
            }

            int top = -1;
            for (int i = 0; i <= cols; i++) {
                while (top != -1 && heights[stack[top]] >= heights[i]) {
                    int height = heights[stack[top--]];
                    int width = (top == -1) ? i : i - stack[top] - 1;
                    maxArea = Math.max(maxArea, height * width);
                }
                stack[++top] = i;
            }
        }
        return maxArea;
    }
}