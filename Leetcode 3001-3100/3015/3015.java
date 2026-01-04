// Leetcode 3015: Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates the number of pairs of houses (i, j) such that the shortest distance between them is `k`.
     * @param n The total number of houses, labeled from 1 to n.
     * @param x The first special house.
     * @param y The second special house.
     * @return An array `result` of length `n`, where `result[k-1]` is the number of pairs of houses with shortest distance `k`.
     */
    public int[] countOfPairs(int n, int x, int y) {
        int[] result = new int[n];
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                int direct = Math.abs(i - j);
                int viaXY = Math.abs(i - x) + 1 + Math.abs(j - y);
                int viaYX = Math.abs(i - y) + 1 + Math.abs(j - x);
                int minDistance = Math.min(direct, Math.min(viaXY, viaYX));
                result[minDistance - 1] += 2;
            }
        }
        return result;
    }
}