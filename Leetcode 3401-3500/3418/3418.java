// Leetcode 3418: Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
// Solved on 2nd of April, 2026
class Solution {
    /**
     * Calculates the maximum amount of money a robot can earn moving from (0,0) to (m-1, n-1).
     * The robot can neutralize up to two negative coin cells to zero.
     * @param coins A 2D grid representing the amount of money in each cell.
     * @return The maximum profit the robot can achieve.
     */
    public int maximumAmount(int[][] coins) {
        int m = coins.length;
        int n = coins[0].length;
        int[][] prev = new int[n][3];
        int[][] curr = new int[n][3];
        int inf = -1000000000;
        
        for (int j = 0; j < n; j++) {
            prev[j][0] = inf;
            prev[j][1] = inf;
            prev[j][2] = inf;
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                curr[j][0] = inf;
                curr[j][1] = inf;
                curr[j][2] = inf;
                
                if (i == 0 && j == 0) {
                    curr[0][0] = coins[0][0];
                    if (coins[0][0] < 0) {
                        curr[0][1] = 0;
                    }
                    continue;
                }
                
                int val = coins[i][j];
                
                for (int k = 0; k < 3; k++) {
                    int top = (i > 0) ? prev[j][k] : inf;
                    int left = (j > 0) ? curr[j - 1][k] : inf;
                    int maxPrev = Math.max(top, left);
                    
                    if (maxPrev != inf) {
                        curr[j][k] = Math.max(curr[j][k], maxPrev + val);
                    }
                    
                    if (val < 0 && k > 0) {
                        int topPrev = (i > 0) ? prev[j][k - 1] : inf;
                        int leftPrev = (j > 0) ? curr[j - 1][k - 1] : inf;
                        int maxPrevK = Math.max(topPrev, leftPrev);
                        
                        if (maxPrevK != inf) {
                            curr[j][k] = Math.max(curr[j][k], maxPrevK);
                        }
                    }
                }
            }
            
            for (int j = 0; j < n; j++) {
                prev[j][0] = curr[j][0];
                prev[j][1] = curr[j][1];
                prev[j][2] = curr[j][2];
            }
        }
        
        int ans = curr[n - 1][0];
        ans = Math.max(ans, curr[n - 1][1]);
        ans = Math.max(ans, curr[n - 1][2]);
        
        return ans;
    }
}