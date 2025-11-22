// Leetcode 2587: Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/
// Solved on 22nd of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Rearranges the array `nums` to maximize the prefix score.
     * The prefix score is the number of non-negative prefix sums.
     * @param nums The input array of integers.
     * @return The maximum possible prefix score after rearranging `nums`.
     */
    public int maxScore(int[] nums) {
        Arrays.sort(nums);
        long sum = 0;
        int score = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            sum += nums[i];
            if (sum > 0) {
                score++;
            } else {
                return score;
            }
        }
        return score;
    }
}