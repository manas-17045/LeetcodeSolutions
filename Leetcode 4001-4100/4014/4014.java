// Leetcode 4014: Minimum Total Price After Applying Discounts
// https://leetcode.com/problems/minimum-total-price-after-applying-discounts/
// Solved on 6th of September, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum total price by optimally assigning discounts
     * to the most expensive items.
     *
     * @param prices the array of prices for each item
     * @param discounts the array of percentage discounts available
     * @return the minimum total price after applying the discounts
     */
    public double minPrice(int[] prices, int[] discounts) {
        Arrays.sort(prices);
        Arrays.sort(discounts);

        double totalPrice = 0.0;
        int priceIndex = prices.length - 1;
        int discountIndex = discounts.length - 1;

        while (priceIndex >= 0 && discountIndex >= 0) {
            totalPrice += (prices[priceIndex] * (100.0 - discounts[discountIndex])) / 100.0;
            priceIndex--;
            discountIndex--;
        }

        while (priceIndex >= 0) {
            totalPrice += prices[priceIndex];
            priceIndex--;
        }

        return totalPrice;
    }
}