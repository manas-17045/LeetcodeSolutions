// Leetcode 3675: Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/
// Solved on 28th of December, 2025
class Solution {
    /**
     * Given a string s, return the minimum number of operations to transform it into a string of all 'a's.
     * An operation consists of choosing a character and replacing all occurrences of it with the next character in the alphabet.
     * @param s The input string.
     * @return The minimum number of operations.
     */
    public int minOperations(String s) {
        int minChar = 'z' + 1;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c != 'a') {
                if (c < minChar) {
                    minChar = c;
                    if (minChar == 'b') {
                        return 25;
                    }
                }
            }
        }

        if (minChar > 'z') {
            return 0;
        }

        return 'z' - minChar + 1;
    }
}