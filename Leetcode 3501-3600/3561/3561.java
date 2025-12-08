// Leetcode 3561: Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/
// Solved on 8th of December, 2025
class Solution {
    /**
     * Given a string s, remove adjacent characters that are consecutive in the alphabet (e.g., 'a' and 'b', 'z' and 'a').
     * @param s The input string.
     * @return The resulting string after all possible removals.
     */
    public String resultingString(String s) {
        StringBuilder stack = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (stack.length() > 0) {
                char last = stack.charAt(stack.length() - 1);
                if (Math.abs(last - c) == 1 || (last == 'a' && c == 'z') || (last == 'z' && c == 'a')) {
                    stack.deleteCharAt(stack.length() - 1);
                    continue;
                }
            }
            stack.append(c);
        }
        return stack.toString();
    }
}