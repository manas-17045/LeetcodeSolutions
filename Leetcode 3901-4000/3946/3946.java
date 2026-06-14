// Leetcode 3946: Maximum Number of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
// Solved on 14th of June, 2026
class Solution {
    /**
     * Calculates the maximum number of items that can be purchased within a given budget.
     * @param items A 2D array where items[i][0] is the factor and items[i][1] is the price.
     * @param budget The total budget available for purchases.
     * @return The maximum number of items that can be bought.
     */
    public int maximumSaleItems(int[][] items, int budget) {
        int maxFactor = 1500;
        int[] factorCounts = new int[maxFactor + 1];
        for (int[] item : items) {
            factorCounts[item[0]]++;
        }
        int[] totalMultiples = new int[maxFactor + 1];
        for (int f = 1; f <= maxFactor; f++) {
            for (int k = f; k <= maxFactor; k += f) {
                totalMultiples[f] += factorCounts[k];
            }
        }
        int[] dp = new int[budget + 1];
        for (int[] item : items) {
            int factor = item[0];
            int price = item[1];
            int count = totalMultiples[factor];
            for (int w = budget; w >= price; w--) {
                if (dp[w - price] + count > dp[w]) {
                    dp[w] = dp[w - price] + count;
                }
            }
            for (int w = price; w <= budget; w++) {
                if (dp[w - price] + 1 > dp[w]) {
                    dp[w] = dp[w - price] + 1;
                }
            }
        }
        return dp[budget];
    }
}