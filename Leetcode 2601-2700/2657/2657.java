// Leetcode 2657: Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
// Solved on 20th of May, 2026
class Solution {
    /**
     * Finds the prefix common array of two permutations.
     *
     * @param A The first input integer array (permutation).
     * @param B The second input integer array (permutation).
     * @return An array where result[i] is the count of numbers present in both A[0...i] and B[0...i].
     */
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] result = new int[n];
        int[] counts = new int[n + 1];
        int common = 0;

        for (int i = 0; i < n; i++) {
            counts[A[i]]++;
            if (counts[A[i]] == 2) {
                common++;
            }

            counts[B[i]]++;
            if (counts[B[i]] == 2) {
                common++;
            }

            result[i] = common;
        }

        return result;
    }
}