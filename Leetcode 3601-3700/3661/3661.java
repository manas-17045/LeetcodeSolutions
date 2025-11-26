// Leetcode 3661: Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/
// Solved on 25th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum number of walls that can be destroyed by a set of robots.
     * @param robots An array representing the positions of the robots.
     * @param distance An array representing the maximum distance each robot can destroy walls from its position.
     * @param walls An array representing the positions of the walls.
     * @return The maximum number of walls that can be destroyed.
     */
    public int maxWalls(int[] robots, int[] distance, int[] walls) {
        int n = robots.length;
        int[][] bots = new int[n][2];
        for (int i = 0; i < n; i++) {
            bots[i][0] = robots[i];
            bots[i][1] = distance[i];
        }
        
        Arrays.sort(bots, (a, b) -> Integer.compare(a[0], b[0]));
        Arrays.sort(walls);
        
        int[][] dp = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            int pos = bots[i][0];
            int dist = bots[i][1];
            int prevPos = (i > 0) ? bots[i - 1][0] : Integer.MIN_VALUE;
            
            long leftStart = Math.max((long)prevPos + 1, (long)pos - dist);
            long leftEnd = pos;
            int wallsLeft = countRange(walls, leftStart, leftEnd);
            
            if (i == 0) {
                dp[i][0] = wallsLeft;
            } else {
                int prevLeftTotal = dp[i - 1][0] + wallsLeft;
                
                int prevDist = bots[i - 1][1];
                long prevRightEnd = Math.min((long)prevPos + prevDist, (long)pos - 1);
                
                int gainFromCurr;
                if (prevRightEnd < leftStart) {
                    gainFromCurr = wallsLeft;
                } else {
                    gainFromCurr = countRange(walls, prevRightEnd + 1, pos);
                }
                
                int prevRightTotal = dp[i - 1][1] + gainFromCurr;
                dp[i][0] = Math.max(prevLeftTotal, prevRightTotal);
            }
            
            long nextPos = (i < n - 1) ? bots[i + 1][0] : Long.MAX_VALUE;
            long rightStart = pos;
            long rightEnd = Math.min((long)pos + dist, nextPos - 1);
            int wallsRight = countRange(walls, rightStart, rightEnd);
            
            if (i == 0) {
                dp[i][1] = wallsRight;
            } else {
                dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][1]) + wallsRight;
            }
        }
        
        return Math.max(dp[n - 1][0], dp[n - 1][1]);
    }
    
    private int countRange(int[] walls, long start, long end) {
        if (start > end) {
            return 0;
        }
        return countLTE(walls, end) - countLTE(walls, start - 1);
    }
    
    private int countLTE(int[] arr, long val) {
        if (val > Integer.MAX_VALUE) {
            return arr.length;
        }
        if (val < Integer.MIN_VALUE) {
            return 0;
        }
        
        int idx = Arrays.binarySearch(arr, (int)val);
        if (idx >= 0) {
            return idx + 1;
        } else {
            return -(idx + 1);
        }
    }
}