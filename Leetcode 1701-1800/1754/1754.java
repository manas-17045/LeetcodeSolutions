// Leetcode 1754: Largest Merge Of Two Strings
// https://leetcode.com/problems/largest-merge-of-two-strings/
// Solved on 19th of November, 2025
class Solution {
    /**
     * Generates the largest possible merge of two strings.
     * @param word1 The first string.
     * @param word2 The second string.
     * @return The largest merge string.
     */
    public String largestMerge(String word1, String word2) {
        StringBuilder merge = new StringBuilder();
        int i = 0;
        int j = 0;
        int m = word1.length();
        int n = word2.length();
        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();

        while (i < m && j < n) {
            if (isLarger(w1, i, w2, j)) {
                merge.append(w1[i++]);
            } else {
                merge.append(w2[j++]);
            }
        }

        if (i < m) {
            merge.append(w1, i, m - i);
        }
        if (j < n) {
            merge.append(w2, j, n - j);
        }

        return merge.toString();
    }

    private boolean isLarger(char[] w1, int i, char[] w2, int j) {
        int m = w1.length;
        int n = w2.length;
        while (i < m && j < n) {
            if (w1[i] != w2[j]) {
                return w1[i] > w2[j];
            }
            i++;
            j++;
        }
        return (m - i) >= (n - j);
    }
}