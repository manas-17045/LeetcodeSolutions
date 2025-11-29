// Leetcode 2507: Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
// Solved on 29th of November, 2025
class Solution {
    /**
     * Calculates the smallest value reachable by repeatedly replacing a number with the sum of its prime factors.
     * @param n The initial integer.
     * @return The smallest value after the replacement process stabilizes.
     */
    public int smallestValue(int n) {
        while (true) {
            int sum = 0;
            int temp = n;
            for (int i = 2; i * i <= temp; i++) {
                while (temp % i == 0) {
                    sum += i;
                    temp /= i;
                }
            }
            if (temp > 1) {
                sum += temp;
            }
            if (sum == n) {
                return n;
            }
            n = sum;
        }
    }
}