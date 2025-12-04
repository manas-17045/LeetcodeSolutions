// Leetcode 3566: Partition Array into Two Equal product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/
// Solved on 3rd of December, 2025
class Solution {
    public boolean checkEqualPartitions(int[] nums, long target) {
        /**
         * Checks if the given array `nums` can be partitioned into two subsets such that the product of elements in each subset equals the `target`.
         * @param nums The input array of integers.
         * @param target The target product for each subset.
         * @return True if such a partition is possible, false otherwise.
         */
        int n = nums.length;
        int limit = 1 << (n - 1);
        for (int i = 1; i < limit; i++) {
            long product1 = 1;
            long product2 = 1;
            boolean possible = true;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    product1 *= nums[j];
                    if (product1 > target) {
                        possible = false;
                        break;
                    }
                } else {
                    product2 *= nums[j];
                    if (product2 > target) {
                        possible = false;
                        break;
                    }
                }
            }
            if (possible && product1 == target && product2 == target) {
                return true;
            }
        }
        return false;
    }
}