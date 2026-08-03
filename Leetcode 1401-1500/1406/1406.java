// Leetcode 1406: Stone Game III
// https://leetcode.com/problems/stone-game-iii/
// Solved on 3rd of August, 2026
class Solution {
    /**
     * Determines the winner of Stone Game III using dynamic programming.
     * 
     * @param stoneValue The values of the stones.
     * @return The winner of the game ("Alice", "Bob", or "Tie").
     */
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int nextOne = 0;
        int nextTwo = 0;
        int nextThree = 0;

        for (int i = n - 1; i >= 0; i--) {
            int currentSum = 0;
            int maxDifference = Integer.MIN_VALUE;

            for (int k = 1; k <= 3 && i + k <= n; k++) {
                currentSum += stoneValue[i + k - 1];
                int nextVal = (k == 1) ? nextOne : (k == 2 ? nextTwo : nextThree);
                maxDifference = Math.max(maxDifference, currentSum - nextVal);
            }

            nextThree = nextTwo;
            nextTwo = nextOne;
            nextOne = maxDifference;
        }

        if (nextOne > 0) {
            return "Alice";
        }
        if (nextOne < 0) {
            return "Bob";
        }
        return "Tie";
    }
}