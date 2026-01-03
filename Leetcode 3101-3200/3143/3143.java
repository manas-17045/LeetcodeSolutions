// Leetcode 3143: Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/
// Solved on 3rd of January, 2026
class Solution {
    /**
     * Calculates the maximum number of points that can be inside a square centered at the origin,
     * such that no two points with the same character are inside the square, and the square is as large as possible.
     * @param points An array of 2D integer coordinates [x, y] for each point.
     * @param s A string where s.charAt(i) is the character associated with points[i].
     * @return The maximum number of points inside the square.
     */
    public int maxPointsInsideSquare(int[][] points, String s) {
        int[] minDistance = new int[26];
        int[] secondMinDistance = new int[26];

        for (int i = 0; i < 26; i++) {
            minDistance[i] = Integer.MAX_VALUE;
            secondMinDistance[i] = Integer.MAX_VALUE;
        }

        int length = points.length;
        for (int i = 0; i < length; i++) {
            int x = points[i][0];
            int y = points[i][1];
            int distance = Math.max(Math.abs(x), Math.abs(y));
            int index = s.charAt(i) - 'a';

            if (distance < minDistance[index]) {
                secondMinDistance[index] = minDistance[index];
                minDistance[index] = distance;
            } else if (distance < secondMinDistance[index]) {
                secondMinDistance[index] = distance;
            }
        }

        int limit = Integer.MAX_VALUE;
        for (int distance : secondMinDistance) {
            if (distance < limit) {
                limit = distance;
            }
        }

        int count = 0;
        for (int distance : minDistance) {
            if (distance < limit) {
                count++;
            }
        }

        return count;
    }
}