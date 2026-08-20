// Leetcode 3998: Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/
// Solved on 20th of August, 2026
class Solution {
    /**
     * Determines whether each pattern string in an array (containing '0', '1', and '?' characters) 
     * can be transformed to match the target binary string's one-count and prefix constraints by 
     * replacing '?' wildcards with '0' or '1'.
     * 
     * @param s     The target binary string consisting of '0' and '1'.
     * @param strs  An array of candidate strings of equal length composed of '0', '1', and '?' characters.
     * @return      A boolean array where each entry is true if the corresponding string can be 
     *              validly transformed to match s, and false otherwise.
     */
    public boolean[] transformStr(String s, String[] strs) {
        int n = s.length();
        int totalOnes = 0;
        int[] prefixS = new int[n];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                totalOnes++;
            }
            prefixS[i] = totalOnes;
        }

        int m = strs.length;
        boolean[] ans = new boolean[m];

        for (int i = 0; i < m; i++) {
            String str = strs[i];
            int countOnes = 0;
            int countQues = 0;

            for (int j = 0; j < n; j++) {
                char c = str.charAt(j);
                if (c == '1') {
                    countOnes++;
                } else if (c == '?') {
                    countQues++;
                }
            }

            int neededOnes = totalOnes - countOnes;
            if (neededOnes < 0 || neededOnes > countQues) {
                ans[i] = false;
                continue;
            }

            int quesAsZero = countQues - neededOnes;
            int seenQues = 0;
            int currentOnes = 0;
            boolean isValid = true;

            for (int j = 0; j < n; j++) {
                char c = str.charAt(j);
                if (c == '1') {
                    currentOnes++;
                } else if (c == '?') {
                    seenQues++;
                    if (seenQues > quesAsZero) {
                        currentOnes++;
                    }
                }

                if (currentOnes > prefixS[j]) {
                    isValid = false;
                    break;
                }
            }

            ans[i] = isValid;
        }

        return ans;
    }
}