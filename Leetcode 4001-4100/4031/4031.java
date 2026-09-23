// Leetcode 4031: Find All Numbers Disappeared in an Array II
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/
// Solved on 23rd of September, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Identifies all contiguous ranges of missing integers within the inclusive
     * range [lower, upper] that do not appear in the given integer array.
     *
     * @param nums the array of integers to inspect
     * @param lower the inclusive lower boundary of the target range
     * @param upper the inclusive upper boundary of the target range
     * @return a list of pairs where each pair [start, end] represents a contiguous
     *         range of missing integers in ascending order
     */
    public List<List<Integer>> findDisappearedNumbers(int[] nums, int lower, int upper) {
        int rangeLength = upper - lower + 1;
        boolean[] present = new boolean[rangeLength];

        for (int num : nums) {
            if (num >= lower && num <= upper) {
                present[num - lower] = true;
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        int index = 0;

        while (index < rangeLength) {
            if (present[index]) {
                index++;
                continue;
            }

            int start = lower + index;
            while (index < rangeLength && !present[index]) {
                index++;
            }
            int end = lower + index - 1;

            result.add(Arrays.asList(start, end));
        }

        return result;
    }
}