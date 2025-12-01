// Leetcode 1648: Sell Diminishing-Valued Colored Balls
// https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
// Solved on 29th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum profit that can be obtained by selling `orders` colored balls.
     *
     * @param inventory An array where `inventory[i]` represents the number of balls of the i-th color.
     * @param orders The total number of balls to sell.
     * @return The maximum profit, modulo 10^9 + 7.
     */
    public int maxProfit(int[] inventory, int orders) {
        Arrays.sort(inventory);
        long total = 0;
        long mod = 1000000007;
        int n = inventory.length;

        for (int i = n - 1; i >= 0; i--) {
            long cur = inventory[i];
            long next = (i > 0) ? inventory[i - 1] : 0;
            long count = n - i;
            long diff = cur - next;
            long items = count * diff;

            if (orders >= items) {
                long sum = (cur + next + 1) * diff / 2;
                total = (total + (sum % mod) * count) % mod;
                orders -= items;
            } else {
                long rows = orders / count;
                long rem = orders % count;
                long last = cur - rows;
                long sum = (cur + last + 1) * rows / 2;
                total = (total + (sum % mod) * count) % mod;
                total = (total + last * rem) % mod;
                break;
            }
        }

        return (int) total;
    }
}