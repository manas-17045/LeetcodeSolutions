// Leetcode 2786: Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/
// Solved on 24th of November, 2025
class Solution {
    /**
     * Calculates the maximum score achievable by visiting array positions.
     * @param nums The input array of integers.
     * @param x The penalty for switching between even and odd numbers.
     * @return The maximum score.
     */
    public long maxScore(int[] nums, int x) {
        long evenMax = nums[0];
        long oddMax = nums[0];

        if (nums[0] % 2 == 0) {
            oddMax -= x;
        } else {
            evenMax -= x;
        }

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                evenMax = nums[i] + Math.max(evenMax, oddMax - x);
            } else {
                oddMax = nums[i] + Math.max(oddMax, evenMax - x);
            }
        }

        return Math.max(evenMax, oddMax);
    }
}