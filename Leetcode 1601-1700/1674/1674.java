// Leetcode 1674: Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
// Solved on 13th of May, 2026
class Solution {
    /**
     * Calculates the minimum number of moves to make an array complementary.
     * An array is complementary if there exists an integer T such that nums[i] + nums[n-1-i] = T for all i.
     *
     * @param nums  An array of integers of even length.
     * @param limit Each element in the array can be modified to any integer between 1 and limit.
     * @return The minimum number of moves required.
     */
    public int minMoves(int[] nums, int limit) {
        int n = nums.length;
        int[] diff = new int[limit * 2 + 2];
        for (int i = 0; i < n / 2; i++) {
            int a = Math.min(nums[i], nums[n - 1 - i]);
            int b = Math.max(nums[i], nums[n - 1 - i]);
            diff[a + 1] -= 1;
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
            diff[b + limit + 1] += 1;
        }
        int minMoves = n;
        int currentMoves = n;
        for (int i = 2; i <= limit * 2; i++) {
            currentMoves += diff[i];
            minMoves = Math.min(minMoves, currentMoves);
        }
        return minMoves;
    }
}