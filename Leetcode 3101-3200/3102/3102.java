// Leetcode 3102: Minimize Manhattan Distance
// https://leetcode.com/problems/minimize-manhattan-distance/
// Solved on 19th of November, 2025
class Solution {
    /**
     * Calculates the minimum possible maximum Manhattan distance between any two points after removing one point.
     *
     * @param points A 2D array where each inner array represents a point [x, y].
     * @return The minimum maximum Manhattan distance.
     */
    public int minimumDistance(int[][]] points) {
        int n = points.length;
        int maxSumIdx = 0, minSumIdx = 0, maxDiffIdx = 0, minDiffIdx = 0;

        for (int i = 1; i < n; i++) {
            int sum = points[i][0] + points[i][1];
            int diff = points[i][0] - points[i][1];
            
            int maxSum = points[maxSumIdx][0] + points[maxSumIdx][1];
            int minSum = points[minSumIdx][0] + points[minSumIdx][1];
            int maxDiff = points[maxDiffIdx][0] - points[maxDiffIdx][1];
            int minDiff = points[minDiffIdx][0] - points[minDiffIdx][1];

            if (sum > maxSum) {
                maxSumIdx = i;
            }
            if (sum < minSum) {
                minSumIdx = i;
            }
            if (diff > maxDiff) {
                maxDiffIdx = i;
            }
            if (diff < minDiff) {
                minDiffIdx = i;
            }
        }

        int[] candidates = {maxSumIdx, minSumIdx, maxDiffIdx, minDiffIdx};
        int minMaxDist = Integer.MAX_VALUE;

        for (int skipIdx : candidates) {
            int currentMaxSum = Integer.MIN_VALUE;
            int currentMinSum = Integer.MAX_VALUE;
            int currentMaxDiff = Integer.MIN_VALUE;
            int currentMinDiff = Integer.MAX_VALUE;

            for (int i = 0; i < n; i++) {
                if (i == skipIdx) {
                    continue;
                }

                int sum = points[i][0] + points[i][1];
                int diff = points[i][0] - points[i][1];

                currentMaxSum = Math.max(currentMaxSum, sum);
                currentMinSum = Math.min(currentMinSum, sum);
                currentMaxDiff = Math.max(currentMaxDiff, diff);
                currentMinDiff = Math.min(currentMinDiff, diff);
            }

            int maxDist = Math.max(currentMaxSum - currentMinSum, currentMaxDiff - currentMinDiff);
            minMaxDist = Math.min(minMaxDist, maxDist);
        }

        return minMaxDist;
    }
}