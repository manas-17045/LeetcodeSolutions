// Leetcode 1793: Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/
// Solved on 8th of November, 2025
class Solution {
    /**
     * Calculates the maximum score of a "good" subarray.
     * A subarray `(i, j)` is good if `i <= k <= j`.
     * The score of a subarray is `min(nums[i..j]) * (j - i + 1)`.
     * @param nums The input array of integers.
     * @param k The index that must be included in the subarray.
     * @return The maximum possible score.
     */
    public int maximumScore(int[] nums, int k) {
        int n = nums.length;
        int left = k;
        int right = k;
        int minVal = nums[k];
        long ans = (long) minVal;
        while (left > 0 || right < n - 1) {
            int leftVal = left > 0 ? nums[left - 1] : -1;
            int rightVal = right < n - 1 ? nums[right + 1] : -1;
            if (leftVal > rightVal) {
                left--;
                if (nums[left] < minVal){
                    minVal = nums[left];
                }
            } else {
                right++;
                if (nums[right] < minVal){
                    minVal = nums[right];
                }
            }
            long score = (long) minVal * (right - left + 1);
            if (score > ans){
                ans = score;
            }
        }
        return (int) ans;
    }
}