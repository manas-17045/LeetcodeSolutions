// Leetcode 3703: Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/
// Solved on 27th of December, 2025
class Solution {
    /**
     * Removes k-balanced substrings from the input string.
     * A k-balanced substring is defined as 'k' opening parentheses followed by 'k' closing parentheses.
     * @param s The input string.
     * @param k The integer k defining the balance.
     * @return The string after removing all k-balanced substrings.
     */
    public String removeSubstring(String s, int k) {
        char[] stack = new char[s.length()];
        int[] counts = new int[s.length()];
        int top = -1;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            top++;
            stack[top] = c;

            if (top > 0 && stack[top - 1] == c) {
                counts[top] = counts[top - 1] + 1;
            } else {
                counts[top] = 1;
            }

            if (c == ')' && counts[top] == k) {
                int prevIndex = top - k;
                if (prevIndex >= 0 && stack[prevIndex] == '(' && counts[prevIndex] >= k) {
                    top -= 2 * k;
                }
            }
        }

        return new String(stack, 0, top + 1);
    }
}