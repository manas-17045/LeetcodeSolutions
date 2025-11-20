// Leetcode 757: Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/
// Solved on 20th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Given a collection of intervals, find the minimum size of a set S such that for every interval `[a, b]` in intervals,
     * the intersection of S with `[a, b]` has size at least 2.
     * @param intervals An array of intervals, where each interval is `[start, end]`.
     * @return The minimum size of the set S.
     */
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> 
            a[1] != b[1] ? Integer.compare(a[1], b[1]) : Integer.compare(b[0], a[0])
        );

        int count = 0;
        int largest = -1;
        int secondLargest = -1;

        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];

            if (start > largest) {
                count += 2;
                secondLargest = end - 1;
                largest = end;
            } else if (start > secondLargest) {
                count += 1;
                secondLargest = largest;
                largest = end;
            }
        }

        return count;
    }
}