// Leetcode 3649: Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/
// Solved on 29th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the number of "perfect pairs" in an array of integers.
     * A pair (nums[i], nums[j]) is considered perfect if nums[j] <= 2 * nums[i] and i < j.
     * @param nums The input array of integers.
     * @return The total count of perfect pairs.
     */
    public long perfectPairs(int[] pairs) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            nums[i] = Math.abs(nums[i]);
        }

        Arrays.sort(nums);

        long count = 0;
        int right = 0;

        for (int left = 0; left < n; left++) {
            if (right < left) {
                right = left;
            }

            long target = 2L * nums[left];

            while (right + 1 < n && nums[right + 1] <= target) {
                right++;
            }

            count += (right - left);
        }

        return count;
    }
}