// Leetcode: 2541: Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/
// Solved on 27th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to make nums1 equal to nums2.
     * An operation consists of choosing an index i and adding k to nums1[i] and subtracting k from nums1[j] (j != i).
     *
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @param k The value to add/subtract in each operation.
     * @return The minimum number of operations, or -1 if it's impossible to make the arrays equal.
     */
    public long minOperations(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        if (k == 0) {
            for (int i = 0; i < n; i++) {
                if (nums1[i] != nums2[i]) {
                    return -1;
                }
            }
            return 0;
        }

        long operations = 0;
        long balance = 0;

        for (int i = 0; i < n; i++) {
            long diff = nums1[i] - nums2[i];
            if (diff % k != 0) {
                return -1;
            }
            long count = diff / k;
            if (count > 0) {
                operations += count;
            }
            balance += count;
        }

        if (balance != 0) {
            return -1;
        }

        return operations;
    }
}