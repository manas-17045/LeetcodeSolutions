// Leetcode 3919: Minimum Cost to Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/
// Solved on 19th of May, 2026
class Solution {
    /**
     * Calculates the minimum cost to move between indices based on proximity rules.
     * 
     * @param nums An array of integers representing positions.
     * @param queries A 2D array where each query is [startIdx, endIdx].
     * @return An array of integers containing the minimum cost for each query.
     */
    public int[] minCost(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] prefRight = new int[n];
        int[] prefLeft = new int[n];
        
        for (int i = 0; i < n - 1; i++) {
            boolean moveRight = false;
            if (i == 0) {
                moveRight = true;
            } else {
                int leftDiff = nums[i] - nums[i - 1];
                int rightDiff = nums[i + 1] - nums[i];
                if (leftDiff > rightDiff) {
                    moveRight = true;
                }
            }
            prefRight[i + 1] = prefRight[i] + (moveRight ? 1 : nums[i + 1] - nums[i]);
        }
        
        for (int i = n - 1; i > 0; i--) {
            boolean moveLeft = false;
            if (i == n - 1) {
                moveLeft = true;
            } else {
                int leftDiff = nums[i] - nums[i - 1];
                int rightDiff = nums[i + 1] - nums[i];
                if (leftDiff <= rightDiff) {
                    moveLeft = true;
                }
            }
            prefLeft[i - 1] = prefLeft[i] + (moveLeft ? 1 : nums[i] - nums[i - 1]);
        }
        
        int qCount = queries.length;
        int[] result = new int[qCount];
        
        for (int i = 0; i < qCount; i++) {
            int startIdx = queries[i][0];
            int endIdx = queries[i][1];
            
            if (startIdx < endIdx) {
                result[i] = prefRight[endIdx] - prefRight[startIdx];
            } else if (startIdx > endIdx) {
                result[i] = prefLeft[endIdx] - prefLeft[startIdx];
            } else {
                result[i] = 0;
            }
        }
        
        return result;
    }
}