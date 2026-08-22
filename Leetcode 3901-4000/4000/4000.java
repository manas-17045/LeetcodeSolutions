// Leetcode 4000: Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/
// Solved on 22nd of August, 2026
class Solution {
    /**
     * Generates the largest integer with n digits that has a digit sum of s.
     * 
     * @param n The number of digits in the integer.
     * @param s The desired digit sum.
     * @return The largest integer with n digits and digit sum s, or -1 if no such integer exists.
     */
    public int largestInteger(int n, int s) {
        if (s > 9 * n) {
            return -1;
        }
        int result = 0;
        int remainingSum = s;
        for (int i = 0; i < n; i++) {
            int digit = Math.min(9, remainingSum);
            result = result * 10 + digit;
            remainingSum -= digit;
        }
        return result;
    }
}