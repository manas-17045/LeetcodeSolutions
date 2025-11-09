// Leetcode 1833: Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/
// Solved on 9th of November, 2025
class Solution {
    /**
     * Calculates the maximum number of ice cream bars that can be bought with a given amount of coins.
     * @param costs An array of integers representing the cost of each ice cream bar.
     * @param coins An integer representing the total amount of coins available.
     * @return The maximum number of ice cream bars that can be bought.
     */
    public int maxIceCream(int[] costs, int coins) {
        int maxCost = 0;
        for (int c : costs) {
            if (c > maxCost) {
                maxCost = c;
            }
        }
        int[] counts = new int[maxCost + 1];
        for (int c : costs) {
            counts[c]++;
        }
        long remaining = coins;
        int result = 0;
        for (int price = 1; price <= maxCost; price++) {
            int freq = counts[price];
            if (freq == 0) {
                continue;
            }
            if (remaining < price) {
                break;
            }
            long canBuy = Math.min((long) freq, remaining / price);
            result += (int) canBuy;
            remaining -= canBuy * price;
            if (remaining < price) {
                break;
            }
        }
        return result;
    }
}