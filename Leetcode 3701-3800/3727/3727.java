// Leetcode 3727: Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/
// Solved on 27th of December, 2025
import java.util.Arrays;

classSolution {
    /**
     * Calculates the maximum alternating sum of squares.
     * The problem asks to maximize sum(nums[i]^2) - sum(nums[j]^2) where i and j are distinct indices.
     * @param nums The input array of integers.
     * @return The maximum alternating sum of squares.
     */
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            nums[i] = Math.abs(nums[i]);
        }
        Arrays.sort(nums);
        long score = 0;
        int k = n / 2;
        for (int i = 0; i < n; i++) {
            long val = (long) nums[i] * nums[i];
            if (i < k) {
                score -= val;
            } else {
                score += val;
            }
        }
        return score;
    }
}