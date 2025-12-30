// Leetcode 3612: Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Processes a string with special operations:
     * '*' deletes the last character, '#' duplicates the current string, '%' reverses the string, and other characters are appended.
     * @param s The input string to process.
     * @return The processed string.
     */
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '*') {
                if (sb.length() > 0) {
                    sb.deleteCharAt(sb.length() - 1);
                }
            } else if (c == '#') {
                int currentLength = sb.length();
                for (int j = 0; j < currentLength; j++) {
                    sb.append(sb.charAt(j));
                }
            } else if (c == '%') {
                sb.reverse();
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}