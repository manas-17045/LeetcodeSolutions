// Leetcode 3931: Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/
// Solved on 31st of May, 2026
class Solution {
    /**
     * Checks if the absolute difference between every two adjacent digits in the string is at most 2.
     *
     * @param s The input string consisting of digits.
     * @return True if all adjacent digit differences are <= 2, false otherwise.
     */
    public boolean isAdjacentDiffAtMostTwo(String s) {
        for (int i = 0; i < s.length() - 1; i++) {
            int diff = Math.abs(s.charAt(i) - s.charAt(i + 1));
            if (diff > 2) {
                return false;
            }
        }
        return true;
    }
}