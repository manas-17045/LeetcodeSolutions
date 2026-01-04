// Leetcode 3091: Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to make the sum of array elements greater than or equal to k.
     * The operations are: incrementing an element or duplicating an element.
     * @param k The target sum.
     * @return The minimum number of operations.
     */
    public int minOperations(int k) {
        int root = (int) Math.ceil(Math.sqrt(k));
        int count = (int) Math.ceil((double) k / root);
        return root + count - 2;
    }
}