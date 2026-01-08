// Leetcode 2679: Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/
// Solved on 8th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the sum of maximums from each column after sorting each row.
     * For each row, the elements are sorted in non-decreasing order.
     * Then, for each column, the maximum element among all rows in that column is selected and added to the total score.
     * @param nums The input matrix of integers.
     * @return The total score calculated as described.
     */
    public int matrixSum(int[][] nums) {
        int score = 0;
        for (int i = 0; i < nums.length; i++) {
            Arrays.sort(nums[i]);
        }
        for (int j = 0; j < nums[0].length; j++) {
            int maxVal = 0;
            for (int i = 0; i < nums.length; i++) {
                maxVal = Math.max(maxVal, nums[i][j]);
            }
            score += maxVal;
        }
        return score;
    }
}