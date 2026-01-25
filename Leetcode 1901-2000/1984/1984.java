// Leetcode 1984: Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
// Solved on 25th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum difference between the highest and lowest of k scores.
     *
     * @param nums The array of scores.
     * @param k The number of scores to pick.
     * @return The minimum possible difference.
     */
    public int minimumDiffernce(int[] nums, int k) {
        if (k == 1) {
            return 0;
        }
        Arrays.sort(nums);
        int minDifference = Integer.MAX_VALUE;
        for (int i = 0; i <= nums.length - k; i++) {
            minDifference = Math.min(minDifference, nums[i + k - 1] - nums[i]);
        }
        return minDifference;
    }
}