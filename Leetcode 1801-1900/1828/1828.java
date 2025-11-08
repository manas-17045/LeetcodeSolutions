// Leetcode 1828: Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
// Solved on 8th of November, 2025
class Solution {
    /**
     * For each query circle, counts how many points fall within or on the boundary of that circle.
     *
     * @param points A 2D array where each `points[i] = [xi, yi]` represents a point.
     * @param queries A 2D array where each `queries[j] = [xj, yj, rj]` represents a circle with center `(xj, yj)` and radius `rj`.
     * @return An array `answer` where `answer[j]` is the number of points inside the `j`-th circle.
     */
    public int[] countPoints(int[][] points, int[][] queries) {
        int qLen = queries.length;
        int pLen = points.length;
        int[] result = new int[qLen];
        for (int i = 0; i < qLen; i++) {
            long centerX = queries[i][0];
            long centerY = queries[i][1];
            long radiusSq = (long) queries[i][2] * queries[i][2];
            int count = 0;
            for (int j = 0; j < pLen; j++) {
                long dx = points[j][0] - centerX;
                long dy = points[j][1] - centerY;
                if (dx * dx + dy * dy <= radiusSq) {
                    count++;
                }
            }
            result[i] = count;
        }
        return result;
    }
}