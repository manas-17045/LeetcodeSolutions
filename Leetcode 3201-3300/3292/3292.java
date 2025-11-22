// Leetcode 3292: Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/
// Solved on 22nd of November, 2025
class Solution {
    /**
     * Calculates the minimum number of valid strings from `words` needed to form the `target` string.
     * @param words An array of strings that can be used to form the target.
     * @param target The target string to be formed.
     * @return The minimum number of valid strings required, or -1 if the target cannot be formed.
     */
    public int minValidStrings(String[] words, String target) {
        nt n = target.length();
        int[] maxJump = new int[n];

        // For each word, compute the longest match starting at each position in target
        for (String word : words) {
            int m = word.length();
            char[] s = new char[m + 1 + n];
            
            // Build temporary string: word + # + target
            for (int i = 0; i < m; i++) {
                s[i] = word.charAt(i);
            }
            s[m] = '#';
            for (int i = 0; i < n; i++) {
                s[m + 1 + i] = target.charAt(i);
            }

            int[] z = zFunction(s);

            // Update max match length for each position
            for (int i = 0; i < n; i++) {
                maxJump[i] = Math.max(maxJump[i], z[m + 1 + i]);
            }
        }

        // Jump Game II logic to find minimum segments
        int steps = 0;
        int curr = 0;
        int next = 0;

        for (int i = 0; i < n; i++) {
            // Cannot reach this index
            if (i > next) { 
                return -1;
            } 
            
            next = Math.max(next, i + maxJump[i]);
            
            if (i == curr) {
                steps++;
                curr = next;
                if (curr >= n) return steps;
            }
        }

        return -1;
    }

    // Standard Z-function implementation
    private int[] zFunction(char[] s) {
        int n = s.length;
        int[] z = new int[n];
        for (int i = 1, l = 0, r = 0; i < n; ++i) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                ++z[i];
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }
}