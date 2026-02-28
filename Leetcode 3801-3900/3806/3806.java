// Leetcode 3806: Maximum Bitwise AND After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/
// Solved on 28th of February, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum possible bitwise AND of at least m elements after 
     * performing at most k total increment operations on the array elements.
     *
     * @param nums An array of integers.
     * @param k The maximum total number of increments allowed.
     * @param m The minimum number of elements required to achieve the bitwise AND.
     * @return The maximum possible bitwise AND value.
     */
    public int maximumAND(int[] nums, int k, int m) {
        long ans = 0;
        long[] costs = new long[nums.length];
        for (int b = 30; b >= 0; b--) {
            long target = ans | (1L << b);
            for (int i = 0; i < nums.length; i++) {
                long x = nums[i];
                long diff = target & ~x;
                if (diff == 0) {
                    costs[i] = 0;
                } else {
                    long h = Long.highestOneBit(diff);
                    long maskAbove = ~((h << 1) - 1);
                    long y = (x & maskAbove) | h | (target & (h - 1));
                    costs[i] = y - x;
                }
            }
            Arrays.sort(costs);
            long totalCost = 0;
            boolean possible = true;
            for (int i = 0; i < m; i++) {
                totalCost += costs[i];
                if (totalCost > k) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                ans = target;
            }
        }
        return (int) ans;
    }
}