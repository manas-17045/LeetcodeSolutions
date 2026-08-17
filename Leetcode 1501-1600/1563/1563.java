// Leetcode 1563: Stone Game V
// https:/leetcode.com/problems/stone-game-v/
// Solved on 17th of August, 2026
class Solution {
    int[][] memo;
    int[] prefixSum;

    /**
     * Calculates the maximum score possible in the Stone Game V.
     * 
     * @param stoneValue The values of the stones.
     * @return The maximum score possible.
     */
    public int stoneGameV(int[] stoneValue) {
        int length = stoneValue.length;
        memo = new int[length][length];
        prefixSum = new int[length + 1];
        
        for (int i = 0; i < length; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }
        
        return calculateMax(0, length - 1);
    }

    private int calculateMax(int start, int end) {
        if (start == end) {
            return 0;
        }
        
        if (memo[start][end] != 0) {
            return memo[start][end];
        }
        
        int currentMax = 0;
        
        for (int i = start; i < end; i++) {
            int leftSum = prefixSum[i + 1] - prefixSum[start];
            int rightSum = prefixSum[end + 1] - prefixSum[i + 1];
            
            if (leftSum < rightSum) {
                currentMax = Math.max(currentMax, leftSum + calculateMax(start, i));
            } else if (leftSum > rightSum) {
                currentMax = Math.max(currentMax, rightSum + calculateMax(i + 1, end));
            } else {
                currentMax = Math.max(currentMax, leftSum + Math.max(calculateMax(start, i), calculateMax(i + 1, end)));
            }
        }
        
        memo[start][end] = currentMax;
        return currentMax;
    }
}