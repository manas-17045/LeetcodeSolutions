// Leetcode 3951: Minimum Energy to Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/
// Solved on 21st of June, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum energy required to maintain the brightness level.
     * 
     * @param n The total number of positions.
     * @param brightness The brightness level to maintain.
     * @param intervals A list of intervals where brightness is required.
     * @return The minimum energy required.
     */
    public long minEnergy(int n, int brightness, int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        long totalTime = 0;
        int currentStart = intervals[0][0];
        int currentEnd = intervals[0][1];
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= currentEnd) {
                currentEnd = Math.max(currentEnd, intervals[i][1]);
            } else {
                totalTime += (currentEnd - currentStart + 1);
                currentStart = intervals[i][0];
                currentEnd = intervals[i][1];
            }
        }
        totalTime += (currentEnd - currentStart + 1);
        
        long bulbsNeeded = (brightness + 2L) / 3;
        return bulbsNeeded * totalTime;
    }
}