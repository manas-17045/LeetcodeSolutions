// Leetcode 3947: Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/
// Solved on 14th of June, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum number of items that can be purchased within a given budget.
     * @param items A 2D array where items[i][0] is the factor and items[i][1] is the price.
     * @param budget The total budget available for purchases.
     * @return The maximum number of items that can be obtained.
     */
    public int maximumSaleItems(int[][] items, int budget) {
        int n = items.length;
        int[] count = new int[n + 1];
        int minPrice = Integer.MAX_VALUE;
        
        for (int[] item : items) {
            count[item[0]]++;
            if (item[1] < minPrice) {
                minPrice = item[1];
            }
        }
        
        int[] gainForFactor = new int[n + 1];
        for (int f = 1; f <= n; f++) {
            for (int mult = f; mult <= n; mult += f) {
                gainForFactor[f] += count[mult];
            }
        }
        
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = items[i][1];
            pairs[i][1] = gainForFactor[items[i][0]] - 1;
        }
        
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[0], b[0]));
        
        int totalCopies = 0;
        int remainingBudget = budget;
        long threshold = 2L * minPrice;
        
        for (int[] pair : pairs) {
            int price = pair[0];
            int gain = pair[1];
            
            if (price >= threshold) {
                break;
            }
            
            if (gain > 0) {
                int countToBuy = Math.min(gain, remainingBudget / price);
                totalCopies += countToBuy * 2;
                remainingBudget -= countToBuy * price;
            }
        }
        
        totalCopies += remainingBudget / minPrice;
        return totalCopies;
    }
}