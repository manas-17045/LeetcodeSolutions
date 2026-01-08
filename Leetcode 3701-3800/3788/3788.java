// Leetcode 3788: Maximum Score of a Split
// https://leetcode.com/problems/maximum-score-of-a-split/
// Solved on 8th of January, 2026
class Solution {
    /**
     * Calculates the maximum score of a split.
     * The score of a split is defined as the sum of the first part minus the minimum element of the second part.
     * @param nums The input array of integers.
     * @return The maximum possible score.
     */
    public long maximumScore(int[] nums) {
        int n = nums.length;
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = nums[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
        }

        long maxScore = Long.MIN_VALUE;
        long currentPrefixSum = 0;

        for (int i = 0; i < n - 1; i++) {
            currentPrefixSum += nums[i];
            long currentScore = currentPrefixSum - suffixMin[i + 1];
            if (currentScore > maxScore) {
                maxScore = currentScore;
            }
        }

        return maxScore;
    }
}