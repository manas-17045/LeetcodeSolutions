// Leetcode 2144: Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
// Solved on 1st of June, 2026
class Solution {
    /**
     * Calculates the minimum cost to buy all candies given a "buy two, get one free" discount.
     * The free candy must have a cost less than or equal to the minimum cost of the two purchased candies.
     *
     * @param cost An array of integers representing the cost of each candy.
     * @return The minimum total cost to purchase all candies.
     */
    public int minimumCost(int[] cost) {
        int[] counts = new int[101];
        for (int price : cost) {
            counts[price]++;
        }
        int totalCost = 0;
        int boughtCount = 0;
        for (int i = 100; i >= 1; i--) {
            while (counts[i] > 0) {
                boughtCount++;
                if (boughtCount % 3 != 0) {
                    totalCost += i;
                }
                counts[i]--;
            }
        }
        return totalCost;
    }
}