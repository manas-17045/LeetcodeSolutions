// Leetcode 3047: Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Finds the largest area of a square that can be formed by the intersection of any two rectangles.
     * @param bottomLeft A 2D array where `bottomLeft[i]` represents the [x, y] coordinates of the bottom-left corner of the i-th rectangle.
     * @param topRight A 2D array where `topRight[i]` represents the [x, y] coordinates of the top-right corner of the i-th rectangle.
     * @return The area of the largest square that can be formed within the intersection of any two rectangles.
     *         If no intersection forms a square, returns 0.
     */
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long maxSide = 0;
        int n = bottomLeft.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long minX = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
                long maxX = Math.min(topRight[i][0], topRight[j][0]);
                long minY = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
                long maxY = Math.min(topRight[i][1], topRight[j][1]);

                if (minX < maxX && minY < maxY) {
                    long width = maxX - minX;
                    long height = maxY - minY;
                    long currentSide = Math.min(width, height);
                    if (currentSide > maxSide) {
                        maxSide = currentSide;
                    }
                }
            }
        }
        return maxSide * maxSide;
    }
}