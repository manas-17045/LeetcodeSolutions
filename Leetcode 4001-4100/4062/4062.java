// Leetcode 4062: Transform Array Using Pair Operations
// https://leetcode.com/problems/transform-array-using-pair-operations/
// Solved on 29th of October, 2026
class Solution {
    /**
     * Determines whether the source array can be transformed into the target array
     * using the allowed pair operations.
     *
     * @param source the array of integers to be transformed
     * @param target the array of integers to match
     * @return true if source can be transformed into target, false otherwise
     */
    public boolean canTransform(int[] source, int[] target) {
        long sourceSum = 0;
        long targetSum = 0;

        for (int i = 0; i < source.length; i++) {
            sourceSum += source[i];
            targetSu += target[i];
        }

        return sourceSum == targetSum;
    }
}