// Leetcode 3796: Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/
// Solved on 9th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the maximum possible value in a sequence of length `n` subject to given restrictions and difference constraints.
     * @param n The length of the sequence.
     * @param restrictions A 2D array where each `restriction[i] = {index, limit}` means `vals[index]` cannot exceed `limit`.
     * @param diff An array where `diff[i]` represents the maximum allowed difference between `vals[i+1]` and `vals[i]`.
     * @return The maximum possible value that can be achieved in the sequence.
     */
    public int findMaxVal(int n, int[][] restrictions, int[] diff) {
        int[] vals = new int[n];
        Arrays.fill(vals, Integer.MAX_VALUE);
        vals[0] = 0;

        for (int[] restriction : restrictions) {
            int index = restriction[0];
            int limit = restriction[1];
            vals[index] = Math.min(vals[index], limit);
        }

        for (int i = 0; i < n - 1; i++) {
            vals[i + 1] = Math.min(vals[i + 1], vals[i] + diff[i]);
        }

        int maxVal = vals[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            vals[i] = Math.min(vals[i], vals[i + 1] + diff[i]);
            maxVal = Math.max(maxVal, vals[i]);
        }

        return maxVal;
    }
}