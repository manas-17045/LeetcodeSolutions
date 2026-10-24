// Leetcode 4057: Number of Intersecting Interval Pairs II
// https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii/
// Solved on 24th of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Computes the total number of intersecting interval pairs.
     * Two closed intervals intersect if they share at least one point in common.
     *
     * @param intervals a 2D integer array where each interval is represented by [start, end]
     * @return the number of pairs (i, j) with 0 <= i < j < n that intersect
     */
    public long countIntersectingIntervals(int[][] intervals) {
        int n = intervals.length;
        int[] startPoints = new int[n];
        int[] endPoints = new int[n];

        for (int i = 0; i < n; i++) {
            startPoints[i] = intervals[i][0];
            endPoints[i] = intervals[i][1];
        }

        Arrays.sort(startPoints);
        Arrays.sort(endPoints);

        long totalPairs = 0;
        int endPointer = 0;

        for (int startPointer = 0; startPointer < n; startPointer++) {
            while (endPointer < n && endPoints[endPointer] < startPoints[startPointer]) {
                endPointer++;
            }
            totalPairs += (startPointer - endPointer);
        }

        return totalPairs;
    }
}