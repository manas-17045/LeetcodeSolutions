// Leetcode 2948: Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
// solved on the 29th of August, 2026
import java.util.Arrays;

class Solution {
    /**
     * Constructs the lexicographically smallest array achievable by repeatedly swapping
     * pairs of elements whose absolute difference is at most the specified limit.
     *
     * @param nums the input array of positive integers
     * @param limit the maximum allowed difference between elements for a valid swap
     * @return the lexicographically smallest array obtained after optimal swaps
     */
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        int[][] pairedElements = new int[n][2];

        for (int i = 0; i < n; i++) {
            pairedElements[i][0] = nums[i];
            pairedElements[i][1] = i;
        }

        Arrays.sort(pairedElements, (a, b) -> Integer.compare(a[0], b[0]));

        int[] result = new int[n];
        int groupStart = 0;

        while (groupStart < n) {
            int groupEnd = groupStart;
            while (groupEnd + 1 < n && pairedElements[groupEnd + 1][0] - pairedElements[groupEnd][0] <= limit) {
                groupEnd++;
            }

            int groupSize = groupEnd - groupStart + 1;
            int[] indices = new int[groupSize];

            for (int i = 0; i < groupSize; i++) {
                indices[i] = pairedElements[groupStart + i][1];
            }

            Arrays.sort(indices);

            for (int i = 0; i < groupSize; i++) {
                result[indices[i]] = pairedElements[groupStart + i][0];
            }

            groupStart = groupEnd + 1;
        }

        return result;   
    }
}