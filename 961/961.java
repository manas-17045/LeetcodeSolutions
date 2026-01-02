// Leetcode 961: N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
// Solved on 2nd of January, 2026
class Solution {
    /**
     * Finds the element that appears N times in an array of size 2N.
     * @param nums The input array of integers.
     * @return The element that is repeated N times.
     */
    public int repeatedNTimes(int[] nums) {
        for (int step = 1; step <= 3; step++) {
            for (int i = 0; i < nums.length - step; i++) {
                if (nums[i] == nums[i + step]) {
                    return nums[i];
                }
            }
        }
        return -1;
    }
}