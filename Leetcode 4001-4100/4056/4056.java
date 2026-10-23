// Leetcode 4056: Number of Intersecting Interval Pairs I
// https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/
// Solved on 23rd of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the total number of intersecting interval pairs.
     *
     * @param intervals a 2D array where intervals[i] = [start, end] represents a closed interval
     * @return the number of pairs (i, j) with i < j that intersect
     */
    public int countIntersectingIntervals(int[][] intervals) {
        int intervalCount = intervals.length;
        int[] startPoints = new int[intervalCount];
        int[] endPoints = new int[intervalCount];

        for (int i = 0; i < intervalCount; i++) {
            startPoints[i] = intervals[i][0];
            endPoints[i] = intervals[i][1];
        }

        Arrays.sort(startPoints);
        Arrays.sort(endPoints);

        long disjointPairs = 0;
        int startIndex = 0;

        for (int i = 0; i < intervalCount; i++) {
            while (startIndex < intervalCount && startPoints[startIndex] <= endPoints[i]) {
                startIndex++;
            }
            disjointPairs += (intervalCount - startIndex);
        }

        long totalPairs = (long) intervalCount * (intervalCount - 1) / 2;
        return (int) (totalPairs - disjointPairs);
    }
}