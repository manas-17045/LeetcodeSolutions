// Leetcode 3945: Digit Frequency Score
// https://leetcode.com/problems/digit-frequency-score/
// Solved on 12th of June, 2026
class Solution {
    /**
     * Calculates the sum of the digits of a given integer.
     * @param n The input integer.
     * @return The sum of all digits in n.
     */
    public int digitFrequencyScore(int n) {
        int totalSum = 0;
        while (n > 0) {
            totalSum += n % 10;
            n /= 10;
        }
        return totalSum;
    }
}