// Leetcode 3634: Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/
// Solved on 6th of February, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of removals to make the array balanced.
     * A balanced array is one where the maximum element is at most k times the minimum element.
     *
     * @param nums An array of integers.
     * @param k The multiplier factor for the balance condition.
     * @return The minimum number of elements to remove.
     */
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            long limit = (long) nums[left] * k;
            while (nums[right] > limit) {
                left++;
                limit = (long) nums[left] * k;
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return nums.length - maxLen;
    }
}