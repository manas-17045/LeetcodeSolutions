// Leetcode 3449: Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-score-of-an-array/
// Solved on 15th of December, 2025
class Solution {
    /**
     * Maximizes the minimum game score.
     * @param points An array of integers representing the points.
     * @param m An integer representing the maximum number of moves.
     * @return The maximum possible minimum score.
     */
    public long maxScore(int[] points, int m) {
        long left = 0;
        long right = 2000000000000000L;
        long ans = 0;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (check(points, m, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    private boolean check(int[] points, int m, long target) {
        if (target == 0) {
            return true;
        }
        long moves = 1;
        long currentVisits = 1;
        int n = points.length;
        for (int i = 0; i < n - 1; i++) {
            if (moves > m) {
                return false;
            }
            long required = (target + points[i] - 1) / points[i];
            long extra = Math.max(0, required - currentVisits);
            moves += 2 * extra;
            long nextVisits = extra;
            if (i == n - 2) {
                long requiredLast = (target + points[n - 1] - 1) / points[n - 1];
                if (nextVisits >= requiredLast) {
                    return moves <= m;
                }
            }
            moves++;
            currentVisits = nextVisits + 1;
        }
        if (moves > m) {
            return false;
        }
        long requiredLast = (target + points[n - 1] - 1) / points[n - 1];
        long extraLast = Math.max(0, requiredLast - currentVisits);
        moves += 2 * extraLast;
        return moves <= m;
    }
}