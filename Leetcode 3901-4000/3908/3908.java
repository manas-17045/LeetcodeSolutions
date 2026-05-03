// Leetcode 3908: Valid Digit Number
// https://leetcode.com/problems/valid-digit-number/
// Solved on 3rd of May, 2026
class Solution {
    /**
     * Checks if a number contains a specific digit and ensures it is not the leading digit.
     * 
     * @param n The integer to be checked.
     * @param x The digit to search for within the integer.
     * @return true if x is present in n and x is not the first digit; false otherwise.
     */
    public boolean validDigit(int n, int x) {
        if (n == 0) {
            return false;
        }
        boolean foundDigit = false;
        int firstDigit = -1;
        while (n > 0) {
            firstDigit = n % 10;
            if (firstDigit == x) {
                foundDigit = true;
            }
            n /= 10;
        }
        return foundDigit && firstDigit != x;
    }
}