// Leetcode 1872: Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/ 
// Solved on 24th of August, 2026
class Solution {
    /**
     * Calculates the maximum score difference between Alice and Bob in Stone Game VIII.
     *
     * @param stones an array of integers representing the values of the stones in order
     * @return the maximum score difference (Alice's score - Bob's score) under optimal play
     */
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        for (int i = 1; i < n; i++) {
            stones[i] += stones[i - 1];
        }
        int maxDifference = stones[n - 1];
        for (int i = n - 2; i >= 1; i--) {
            maxDifference = Math.max(maxDifference, stones[i] - maxDifference);
        }
        return maxDifference;
    }
}