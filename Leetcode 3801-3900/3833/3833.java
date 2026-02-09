// Leetcode 3833: Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/
// Solved on 9th of February, 2026
class Solution {
    /**
     * Counts the number of dominant indices in the array.
     * @param nums The input array of integers.
     * @return The total count of dominant indices.
     */
    public int dominantIndices(int[] nums) {
        int ans = 0;
        int sum = 0;
        int len = 0;

        for (int i = nums.length - 1; i >= 0; i--) {
            if (len > 0 && nums[i] * len > sum) {
                ans++;
            }
            sum += nums[i];
            len++;
        }

        return ans;
    }
}