// Leetcode 3111: Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/
// Solved on 4th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of rectangles required to cover all given points.
     * Each rectangle has a fixed width `w` and an infinite height.
     * @param points A 2D array where each `points[i] = [xi, yi]` represents a point.
     * @param w The fixed width of the rectangles.
     * @return The minimum number of rectangles needed to cover all points.
     */
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        int rectangles = 0;
        int lastCoveredX = -1;
        for (int[] point : points) {
            if (point[0] > lastCoveredX) {
                rectangles++;
                lastCoveredX = point[0] + w;
            }
        }
        return rectangles;
    }
}