// Leetcode 1326: Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
// Solved on 30th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of taps to open to water a garden of length `n`.
     * @param n The length of the garden.
     * @param ranges An array where `ranges[i]` denotes the range of the i-th tap.
     * @return The minimum number of taps to open, or -1 if the garden cannot be watered.
     */
    public int minTaps(int n, int[] ranges) {
        int[] maxReach = new int[n + 1];
        for (int i = 0; i < ranges.length; i++) {
            int start = Math.max(0, i - ranges[i]);
            int end = Math.min(n, i + ranges[i]);
            maxReach[start] = Math.max(maxReach[start], end);
        }

        int taps = 0;
        int currentEnd = 0;
        int nextEnd = 0;

        for (int i = 0; i < n; i++) {
            nextEnd = Math.max(nextEnd, maxReach[i]);

            if (i == currentEnd) {
                if (nextEnd <= i) {
                    return -1;
                }
                currentEnd = nextEnd;
                taps++;
            }
        }

        return taps;
    }
}