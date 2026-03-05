// Leetcode 2029: Stone Game IX
// https://leetcode.com/problems/stone-game-ix/
// Solved on 5th of March, 2026
class Solution {
    /**
     * Determines if Alice can win the stone game given the rules of modulo 3 sums.
     * 
     * @param stones An array of integers representing the values of the stones.
     * @return true if Alice has a winning strategy, false otherwise.
     */
    public boolean stoneGameIX(int[] stones) {
        int[] counts = new int[3];
        for (int stine : stones) {
            counts[stone % 3]++;
        }
        
        if (counts[0] % 2 == 0) {
            return counts[1] > 0 && counts[2] > 0;
        } else {
            return Math.abs(counts[1] - counts[2]) > 2;
        }
    }
}