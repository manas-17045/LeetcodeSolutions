// Leetcode 788: Rotated Digits
// https://leetcode.com/problems/rotated-digits/
// Solved on 2nd of May, 2026
class Solution {
    /**
     * Counts how many numbers from 1 to n are "good" after rotation.
     * A number is good if after rotating each digit 180 degrees, it forms a valid different number.
     * @param n The upper bound integer (inclusive).
     * @return The total count of good integers in the range [1, n].
     */
    public int rotatedDigits(int n) {
        int validCount = 0;
        for (int i = 1; i <= n; i++) {
            int current = i;
            boolean hasRotated = false;
            boolean isValid = true;
            while (current > 0) {
                int digit = current % 10;
                if (digit == 3 || digit == 4 || digit == 7) {
                    isValid = false;
                    break;
                }
                if (digit == 2 || digit == 5 || digit == 6 || digit == 9) {
                    hasRotated = true;
                }
                current /= 10;
            }
            if (isValid && hasRotated) {
                validCount++;
            }
        }
        return validCount;
    }
}