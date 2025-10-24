// Leetcode 2048: Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/
// Solved on 24th of October, 2025
class Solution {
    
    /**
     * Finds the smallest numerically balanced number strictly greater than n.
     * A number is numerically balanced if for every digit d present in the number,
     * d appears exactly d times.
     * @param n The input integer.
     * @return The smallest numerically balanced number strictly greater than n, or -1 if none found within a reasonable range.
     */
    public int nextBeautifulNumber(int n) {
        // Start checking from n + 1
        for (int num = n + 1; num <= 10000000; num++) {
            if (isNumericallyBalanced(num)) {
                return num;
            }
        }
        return -1;
    }

    private boolean isNumericallyBalanced(int num) {
        // Count frequency of each digit
        int[] freq = new int[10];
        int temp = num;
        int digitCount = 0;

        while (temp > 0) {
            int digit = temp % 10;
            freq[digit]++;
            digitCount++;
            temp /= 10;
        }

        // Check if each digit appears exactly as many times as its value
        for (int digit = 0; digit <= 9; digit++) {
            if (freq[digit] > 0 && freq[digit] != digit) {
                return false;
            }
        }

        return true;
    }
}