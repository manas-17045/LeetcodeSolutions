// Leetcode 3332: Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/
// Solved on 2nd of January, 2026
class Solution {
    /**
     * Calculates the maximum points a tourist can earn.
     * @param n The number of cities.
     * @param k The number of days.
     * @param stayScore A 2D array where stayScore[i][j] is the points earned for staying in city j on day i.
     * @param travelScore A 2D array where travelScore[i][j] is the points earned for traveling from city i to city j.
     * @return The maximum points the tourist can earn.
     */
    public int maxScore(int n, int k, int[][] stayScore, int[][] travelScore) {
        int[] dp = new int[n];
        int[] nextDp = new int[n];

        for (int i = 0; i < k; i++) {
            for (int curr = 0; curr < n; curr++) {
                int currentMax = 0;
                for (int prev = 0; prev < n; prev++) {
                    int val = dp[prev];
                    if (prev == curr) {
                        val += stayScore[i][curr];
                    } else {
                        val += travelScore[prev][curr];
                    }
                    
                    if (val > currentMax) {
                        currentMax = val;
                    }
                }
                nextDp[curr] = currentMax;
            }
            
            int[] temp = dp;
            dp = nextDp;
            nextDp = temp;
        }

        int maxPoints = 0;
        for (int score : dp) {
            if (score > maxPoints) {
                maxPoints = score;
            }
        }
        
        return maxPoints;
    }
}