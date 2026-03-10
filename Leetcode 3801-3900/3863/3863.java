// Leetcode 3863: Minimum Operations to Sort a String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/
// Solved on 10th of March, 2026
class Solution {
    /**
     * Calculates the minimum number of operations required to sort the given string.
     * 
     * @param s The input string to be sorted.
     * @return The minimum number of operations as an integer.
     */
    public int minOperations(String s) {
        int n = s.length();
        boolean isSorted = true;
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) > s.charAt(i + 1)) {
                isSorted = false;
                break;
            }
        }
        if (isSorted) {
            return 0;
        }
        if (n <= 2) {
            return -1;
        }

        charMaxLeft = s.charAt(0);
        for (int i = 1; i <= n - 2; i++) {
            if (s.charAt(i) > maxLeft) {
                maxLeft = s.charAt(i);
            }
        }
        if (maxLeft <= s.charAt(n - 1)) {
            return 1;
        }

        char minRight = s.charAt(1);
        for (int i = 2; i <= n - 1; i++) {
            if (s.charAt(i) < minRight) {
                minRight = s.charAt(i);
            }
        }
        if (s.charAt(0) <= minRight) {
            return 1;
        }

        boolean isMaxAtStart = true;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) >= s.charAt(0)) {
                isMaxAtStart = false;
                break;
            }
        }

        boolean isMinAtEnd = true;
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) <= s.charAt(n - 1)) {
                isMinAtEnd = false;
                break;
            }
        }

        if (isMaxAtStart && isMinAtEnd) {
            return 3;
        }
        return 2;
    }
}