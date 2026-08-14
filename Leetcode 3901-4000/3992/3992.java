// Leetcode 3992: Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/
// Solved on 14th of August, 2026
class Solution {
    /**
     * Rearranges the characters of a string such that no two identical characters are adjacent and no `x` is followed by a `y`. 
     * 
     * @param s The input string.
     * @param x The first character.
     * @param y The second character.
     * @return The rearranged string.
     */
    public String rearrangeString(String s, char x, char y) {
        int length = s.length();
        char[] result = new char[length];
        int countY = 0;
        int countX = 0;

        for (int i = 0; i < length; i++) {
            char ch = s.charAt(i);
            if (ch == y) {
                countY++;
            } else if (ch == x) {
                countX++;
            }
        }

        int index = 0;
        for (int i = 0; i < countY; i++) {
            result[index++] = y;
        }

        for (int i = 0; i < length; i++) {
            char ch = s.charAt(i);
            if (ch != x && ch != y) {
                result[index++] = ch;
            }
        }

        for (int i = 0; i < countX; i++) {
            result[index++] = x;
        }

        return new String(result);
    }
}