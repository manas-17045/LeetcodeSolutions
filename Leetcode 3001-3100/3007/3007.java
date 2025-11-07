// Leetcode 3007: Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/
// Solved on 7th of November, 2025
class Solution {
    /**
     * Finds the maximum number `num` such that the sum of prices of all numbers from 1 to `num` is less than or equal to `k`.
     * The price of a number is defined as the count of set bits at positions that are multiples of `x`.
     * @param k The maximum allowed sum of prices.
     * @param x The multiplier for bit positions to consider for price calculation.
     * @return The maximum number `num` satisfying the condition.
     */
    public long findMaximumNumber(long k, int x) {
        long low = 0L;
        long high = 1000000000000000000L;
        while (low < high) {
            long mid = low + ((high - low + 1L) >> 1);
            if (accumulatedPrice(mid, x, k) <= k) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private long accumulatedPrice(long n, int x, long limit) {
        long total = 0L;
        for (int p = x; ; p += x) {
            if (p - 1 >= 63){
                break;
            }
            long pow = 1L << (p - 1);
            if (pow > n){
                break;
            }
            long cycle = pow << 1;
            long full = n / cycle;
            long ones = full * pow;
            long rem = n % cycle;
            long extra = rem - pow + 1;
            if (extra > 0){
                ones += extra;
            }
            total += ones;
            if (total > limit){
                return limit + 1;
            }
        }
        return total;
    }
}