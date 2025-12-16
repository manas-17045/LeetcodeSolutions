// Leetcode 3538: Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/
// Solved on 16th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum travel time to merge all items.
     *
     * @param l The length of the track (not directly used in the provided logic, but typically represents a boundary).
     * @param n The number of items.
     * @param k The maximum number of merge operations allowed.
     * @param position An array representing the positions of the items.
     * @param time An array representing the time (or rate) associated with each item.
     * @return The minimum travel time.
     */
    public int minTravelTime(int l, int n, int k, int[] position, int[] time) {
        int[] P = new int[n];
        P[0] = time[0];
        for (int i = 1; i < n; i++) {
            P[i] = P[i - 1] + time[i];
        }

        int[][][] dp = new int[n][n][k + 1];

        int inf = Integer.MAX_VALUE / 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp[i][j], inf);
            }
        }

        for (int i = 1; i < n; i++) {
            int merges = i - 1;
            if (merges <= k) {
                int dist = position[i] - position[0];
                int rate = time[0]; 
                dp[i][0][merges] = dist * rate;
            }
        }

        for (int i = 2; i < n; i++) {
            for (int j = 1; j < i; j++) {
                int newMerges = i - j - 1;
                
                for (int m = newMerges; m <= k; m++) {
                    int prevMerges = m - newMerges;
                    int dist = position[i] - position[j];
                    
                    int bestPrevCost = inf;
                    
                    for (int p = 0; p < j; p++) {
                        if (dp[j][p][prevMerges] != inf) {
                            int rate = P[j] - P[p];
                            int currentCost = dp[j][p][prevMerges] + dist * rate;
                            if (currentCost < bestPrevCost) {
                                bestPrevCost = currentCost;
                            }
                        }
                    }
                    
                    dp[i][j][m] = bestPrevCost;
                }
            }
        }

        int result = inf;
        for (int j = 0; j < n - 1; j++) {
            result = Math.min(result, dp[n - 1][j][k]);
        }

        return result;
    }
}