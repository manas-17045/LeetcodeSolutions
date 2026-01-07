// Leetcode 2772: Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/
// Solved on 7th of January, 2026
class Solution {
    /**
     * Checks if all elements in the array can be made zero by applying a specific operation.
     * The operation involves choosing an index `i` and subtracting 1 from `nums[i]`, `nums[i+1]`, ..., `nums[i+k-1]`.
     * @param nums The input array of integers.
     * @param k The length of the subarray to apply the operation on.
     * @return True if all elements can be made zero, false otherwise.
     */
    public boolean checkArray(int[] nums, int k) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        int currentSub = 0;

        for (int i = 0; i < n; i++) {
            currentSub -= diff[i];
            int required = nums[i] - currentSub;

            if (required == 0) {
                continue;
            }

            if (required < 0 || i + k > n) {
                return false;
            }

            currentSub += required;
            diff[i + k] += required;
        }

        return true;
    }
}