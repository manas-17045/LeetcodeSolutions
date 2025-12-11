// Leetcode 2117: Abbreviating the Product of a Range
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/
// Solved on 11th of December, 2025
class Solution {
    /**
     * Abbreviates the product of a range of integers [left, right].
     *
     * @param left The left bound of the range (inclusive).
     * @param right The right bound of the range (inclusive).
     * @return A string representing the abbreviated product.
     */
    public String abbreviateProduct(int left, int right) {
        long count2 = 0;
        long count5 = 0;
        double logSum = 0;

        for (int i = left; i <= right; i++) {
            logSum += Math.log10(i);
            int temp = i;
            while (temp % 2 == 0) {
                count2++;
                temp /= 2;
            }
            while (temp % 5 == 0) {
                count5++;
                temp /= 5;
            }
        }

        int zeros = (int) Math.min(count2, count5);
        long totalDigits = (long) logSum + 1;
        long remainingDigits = totalDigits - zeros;

        if (remainingDigits <= 10) {
            long current = 1;
            int rem2 = zeros;
            int rem5 = zeros;
            
            for (int i = left; i <= right; i++) {
                long val = i;
                while (rem2 > 0 && val % 2 == 0) {
                    val /= 2;
                    rem2--;
                }
                while (rem5 > 0 && val % 5 == 0) {
                    val /= 5;
                    rem5--;
                }
                current *= val;
            }
            return current + "e" + zeros;
        }

        long suffix = 1;
        int rem2 = zeros;
        int rem5 = zeros;
        long MOD = 100000;
        
        for (int i = left; i <= right; i++) {
            long val = i;
            while (rem2 > 0 && val % 2 == 0) {
                val /= 2;
                rem2--;
            }
            while (rem5 > 0 && val % 5 == 0) {
                val /= 5;
                rem5--;
            }
            suffix = (suffix * val) % MOD;
        }
        
        String suffixStr = String.valueOf(suffix);
        while (suffixStr.length() < 5) {
            suffixStr = "0" + suffixStr;
        }

        double product = 1.0;
        for (int i = left; i <= right; i++) {
            product *= i;
            while (product >= 1e14) {
                product /= 10;
            }
        }
        
        while (product >= 100000) {
            product /= 10;
        }
        int prefix = (int) product;

        return prefix + "..." + suffixStr + "e" + zeros;
    }
}