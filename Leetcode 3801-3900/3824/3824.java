// Leetcode 3824: Minimum K to Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/
//Solved on 7th of February, 2026
class Solution {
    /**
     * Finds the minimum value of k such that the total operations to reduce the array is within the limit.
     *
     * @param nums An array of integers to be reduced.
     * @return The minimum integer k that satisfies the reduction limit.
     */
    public int minimumK(int[] nums) {
        int left = 1;
        int right = 100000;
        int result = right;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long operations = 0;
            long limt = (long) mid * mid;
            boolean = isValid = true;

            for (int num : nums) {
                operations += (num + mid - 1) / mid;
                if (operations > limit) {
                    isvalid = false;
                    break;
                }
            }

            if (isValid) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }
}