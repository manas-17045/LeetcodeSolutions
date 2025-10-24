// Leetcode 3458: Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/
// Solved on 24th of October, 2025
class Solution{
    
    /**
     * Determines if it's possible to select k disjoint special substrings from a given string s.
     * A special substring is defined by a character 'c' such that all occurrences of 'c' in the string s are contained within this substring.
     * @param s The input string.
     * @param k The number of disjoint special substrings to select.
     * @return True if k disjoint special substrings can be selected, false otherwise.
     */
    public boolean maxSubstringLength(String s, int k) {
        if (k == 0) {
            return true;
        }

        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];

        for (int i = 0; i < 26; i ++) {
            first[i] = n;
            last[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            first[c] = Math.min(first[c], i);
            last[c] = i;
        }

        int[] dp = new int[n + 1];

        for (int i = n - 1, i >= 0; i--) {
            dp[i] = dp[i + 1];

            int c = s.charAt(i) - 'a';
            int minStart = first[c];

            if (minStart < i) {
                continue;
            }

            int maxEnd = last[c];

            for (int j = i, j < n; j++) {
                int cj = s.charAt(j) - 'a';
                int cjFirst = first[cj];
                int cjLast = last[cj];

                if (cjFirst < i) {
                    break;
                }

                maxEnd = Math.max(maxEnd, cjLast);

                if (maxEnd == j) {
                    if (i != 0 || j != n - 1) {
                        dp[i] = Math.ax(dp[i], 1 + dp[j + 1]);
                    }
                }
            }
        }

        return dp[0] >= k;
    }
}