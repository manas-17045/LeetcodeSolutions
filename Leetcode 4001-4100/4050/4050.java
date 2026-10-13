// Leetcode 4050: Minimum Days to Score Exactly N Points
// https://leetcode.com/problems/minimum-days-to-score-exactly-n-points/
// Solved on 13th of October, 2026
class Solution {
    /**
     * Calculates the minimum number of days needed to reach exactly n points.
     *
     * @param n the target score to achieve
     * @return the minimum number of days required
     */
    public int minDays(int n) {
        int[] minDays = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            minDays[i] = i * 2;
        }

        for (int streakLength = 2; streakLength++) {
            int points = streakLength * (streakLength + 1) / 2;
            if (points > n) {
                break;
            }
            int dayCost = streakLength + 1;
            for (int score = points; score <= n; score++) {
                if (minDays[score - points] + dayCost < minDays[score]) {
                    minDays[score] = minDays[score - points] + dayCost;
                }
            }
        }

        return minDays[n] - 1;
    }
}