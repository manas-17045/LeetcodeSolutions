// Leetcode 2865: Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/
// Solved on 6th of January, 2026
class Solution {
    /**
     * Calculates the maximum possible sum of heights of a "beautiful" tower configuration.
     * A tower configuration is beautiful if its heights are non-increasing to the left and non-decreasing to the right of a peak.
     * @param heights An array of integers representing the maximum possible heights for each tower.
     * @return The maximum sum of heights achievable for a beautiful tower configuration.
     */
    public long maximumSumOfHeights(int[] heights) {
        long maxSum = 0;
        int n = heights.length;

        for (int i = 0; i < n; i++) {
            long currentSum = heights[i];
            int minHeight = heights[i];

            for (int j = i - 1; j >= 0; j--) {
                minHeight = Math.min(minHeight, heights[j]);
                currentSum += minHeight;
            }

            minHeight = heights[i];

            for (int j = i + 1; j < n; j++) {
                minHeight = Math.min(minHeight, heights[j]);
                currentSum += minHeight;
            }

            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}