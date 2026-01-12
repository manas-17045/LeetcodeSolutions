// Leetcode 1266: Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/
// Solved on 12th of January, 2026
class Solution {
    /**
     * Calculates the minimum time to visit all points in the given order.
     *
     * @param points An array of points, where each point is an array of two integers [x, y].
     * @return The minimum time to visit all points.
     */
    public int minTimeToVisitAllPoints(int[][] points) {
        int totalTime = 0;
        for (int i = 0; i < points.length - 1; i++) {
            int xDiff = Math.abs(points[i][0] - points[i + 1][0]);
            int yDiff = Math.abs(points[i][1] - points[i + 1][1]);
            totalTime += Math.max(xDiff, yDiff);
        }
        return totalTime;
    }
}