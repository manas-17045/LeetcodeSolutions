// Leetcode 3722: Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/
// Solved on 27th of December, 2025
class Solution {
    /**
     * Finds the lexicographically smallest string after performing at most one reverse operation.
     * A reverse operation can be applied to a prefix or a suffix of the string.
     * @param s The input string.
     * @return The lexicographically smallest string achievable.
     */
    public String lexSmallest(String s) {
        int n = s.length();
        String minString = s;

        for (int k = 1; k <= n; k++) {
            StringBuilder sb1 = new StringBuilder(s.substring(0, k));
            String str1 = sb1.reverse().append(s.substring(k)).toString();
            if (str1.compareTo(minString) < 0) {
                minString = str1;
            }

            StringBuilder sb2 = new StringBuilder(s.substring(n - k));
            String str2 = s.substring(0, n - k) + sb2.reverse().toString();
            if (str2.compareTo(minString) < 0) {
                minString = str2;
            }
        }
        
        return minString;
    }
}