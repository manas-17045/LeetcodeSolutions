// Leetcode 3670: Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/
// Solved on 1st of December, 2025
class Solution {
    /**
     * Calculates the maximum product of two integers from the given array that have no common set bits.
     *
     * @param nums An array of non-negative integers.
     * @return The maximum product of two integers with no common bits. If no such pair exists, returns 0.
     */
    public long maxProduct(int[] nums) {
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        int bitLength = 32 - Integer.numberOfLeadingZeros(maxVal);
        int maskSize = 1 << bitLength;
        int[] dp = new int[maskSize];

        for (int num : nums) {
            dp[num] = num;
        }

        for (int i = 0; i < bitLength; i++) {
            for (int mask = 0; mask < maskSize; mask++) {
                if ((mask & (1 << i)) != 0) {
                    dp[mask] = Math.max(dp[mask], dp[mask ^ (1 << i)]);
                }
            }
        }

        long maxProduct = 0;
        int fullMask = maskSize - 1;

        for (int num : nums) {
            int complement = fullMask ^ num;
            maxProduct = Math.max(maxProduct, (long) num * dp[complement]);
        }

        return maxProduct;
    }
}