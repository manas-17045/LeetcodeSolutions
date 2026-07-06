// Leetcode 1288: Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/
// Solved on 6th of July, 2026
import java.util.Arrays;

class Solution {
    /**
     * Removes covered intervals from a list of intervals and returns the number of
     * remaining intervals.
     * 
     * @param intervals The list of intervals.
     * @return The number of remaining intervals.
     */
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        int remainingCount = 0;
        int maxEnd = 0;
        for (int[] curr : intervals) {
            if (curr[1] > maxEnd) {
                remainingCount++;
                maxEnd = curr[1];
            }
        }
        return remainingCount;
    }
}