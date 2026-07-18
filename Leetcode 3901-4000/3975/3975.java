// Leetcode 3975: Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/
// Solved on 18th of July, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Filters occupied intervals to remove those within the free time range.
     * 
     * @param occupiedIntervals The occupied time intervals.
     * @param freeStart The start of the free time range.
     * @param freeEnd The end of the free time range.
     * @return The filtered list of occupied intervals.
     */
    public List<List<Integer>> filterOccupiedIntervals(int[][] occupiedIntervals, int freeStart, int freeEnd) {
        if (occupiedIntervals == null || occupiedIntervals.length == 0) {
            return new ArrayList<>();
        }

        Arrays.sort(occupiedIntervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<List<Integer>> result = new ArrayList<>();
        int currentStart = occupiedIntervals[0][0];
        int currentEnd = occupiedIntervals[0][1];

        for (int i = 1; i < occupiedIntervals.length; i++) {
            int nextStart = occupiedIntervals[i][0];
            int nextEnd = occupiedIntervals[i][1];

            if (nextStart <= currentEnd + 1) {
                currentEnd = Math.max(currentEnd, nextEnd);
            } else {
                addFiltered(result, currentStart, currentEnd, freeStart, freeEnd);
                currentStart = nextStart;
                currentEnd = nextEnd;
            }
        }

        addFiltered(result, currentStart, currentEnd, freeStart, freeEnd);
        return result;
    }

    private void addFiltered(List<List<Integer>> result, int start, int end, int freeStart, int freeEnd) {
        if (end < freeStart || start > freeEnd) {
            result.add(Arrays.asList(start, end));
        } else {
            if (start < freeStart) {
                result.add(Arrays.asList(start, freeStart - 1));
            }
            if (end > freeEnd) {
                result.add(Arrays.asList(freeEnd + 1, end));
            }
        }
    }
}