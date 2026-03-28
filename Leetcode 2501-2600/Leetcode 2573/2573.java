// Leetcode 2573: Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/
// Solved on 28th of March, 2026
class Solution {
    /**
     * Finds the lexicographically smallest string that satisfies the given LCP matrix.
     * 
     * @param lcp A 2D integer array representing the longest common prefix between suffixes.
     * @return The resulting string if it exists and is valid; otherwise, an empty string.
     */
    public String findTheString(int[][] lcp) {
        int n = lcp.length;
        char[] arr = new char[n];
        char c = 'a';

        for (int i = 0; i < n; i++) {
            if (arr[i] != 0) {
                continue;
            }
            if (c > 'z') {
                return "";
            }
            arr[i] = c;
            for (int j = i + 1; j < n; j++) {
                if (lcp[i][j] > 0) {
                    arr[j] = c;
                }
            }
            c++;
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int val = 0;
                if (arr[i] == arr[j]) {
                    val = 1 + (i + 1 < n && j + 1 < n ? lcp[i + 1][j + 1] : 0);
                }
                if (lcp[i][j] != val) {
                    return "";
                }
            }
        }

        return new String(arr);
    }
}