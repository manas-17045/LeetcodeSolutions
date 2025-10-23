// Leetcode 3298: Count Substrings That Can Be Rearranged to Contain a String II
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
// Solved on 23rd of October, 2025
class Solution {
    
    /**
     * Counts the number of substrings in word1 that can be rearranged to contain word2.
     * @param word1 The main string to search within.
     * @param word2 The target string whose characters must be present in a substring of word1.
     * @return The total count of such valid substrings.
     */
    public long validSubstringCount(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        if (m > n) return 0L;

        // req[c] = how many of char c ('a'..'z') we still need for current window
        int[] req = new int[26];
        for (int i = 0; i < m; i++) {
            req[word2.charAt(i) - 'a']++;
        }

        // missing = total number of characters still needed (sum of positives in req)
        int missing = 0;
        for (int v : req) missing += v;

        char[] s = word1.toCharArray();
        int r = 0;
        long ans = 0L;

        for (int l = 0; l < n; l++) {
            // Expand r until the window [l, r-1] contains all required characters or r == n
            while (r < n && missing > 0) {
                int idx = s[r] - 'a';
                if (req[idx] > 0) {
                    missing--;
                }
                req[idx]--;
                r++;
            }

            if (missing == 0) {
                // minimal valid window ends at r-1; all windows ending at >= r-1 are valid
                ans += (n - r + 1);
            } else {
                // r == n and still missing > 0: no further windows starting at l or later can be valid
                break;
            }

            // Move left forward: remove s[l] from window
            int idxL = s[l] - 'a';
            req[idxL]++;
            if (req[idxL] > 0) {
                // by incrementing req we re-introduced a missing character
                missing++;
            }
        }

        return ans;
    }
}