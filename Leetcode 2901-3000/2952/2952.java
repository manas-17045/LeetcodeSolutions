// Leetcode 2952: Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
// Solved on 12th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of coins that need to be added to the given set of coins
     * to be able to form any sum from 1 up to the target.
     * @param coins An array of integers representing the available coins.
     * @param target An integer representing the maximum sum that needs to be achievable.
     * @return The minimum number of coins that need to be added.
     */
    public int minimumAddedCoins(int[] coins, int target) {
        Arrays.sort(coins);
        long reach = 0;
        int i = 0;
        int added = 0;
        int n = coins.length;
        while (reach < target) {
            long need = reach + 1;
            if (i < n && coins[i] <= need) {
                reach += coins[i];
                i++;
            } else {
                reach += need;
                added++;
            }
        }
        return added;
    }
}