// Leetcode 3281: Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/
// Solved on 30th of October, 2025
import java.util.Arrays;

class Solution {

    /**
     * Calculates the maximum possible score that can be achieved.
     * @param start An array of integers representing the starting points.
     * @param d An integer representing the maximum allowed difference.
     * @return The maximum possible score.
     */
    public int maxPossibleScore(int[] start, int d) {
        Arrays.sort(start);
        
        int low = 0;
        int high = 2_000_000_000;
        int maxScore = 0;
        
        while (low <= high) {
            int midScore = low + (high - low) / 2;
            
            if (isPossible(start, d, midScore)) {
                maxScore = midScore;
                low = midScore + 1;
            } else {
                high = midScore - 1;
            }
        }
        
        return maxScore;
    }

    private boolean isPossible(int[] start, int d, int score) {
        int n = start.length;
        long previousValue = start[0];
        
        for (int i = 1; i < n; i++) {
            long minNextValue = previousValue + score;
            long intervalStart = start[i];
            long intervalEnd = (long)start[i] + d;
            
            long nextValue = Math.max(minNextValue, intervalStart);
            
            if (nextValue > intervalEnd) {
                return false;
            }
            previousValue = nextValue;
        }
        return true;
    }
}