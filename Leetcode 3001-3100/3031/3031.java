// Leetcode 3031: Minimum Time to Revert Word to InitialState II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
// Solved on 12th of December, 2025
class Solution {
    /**
     * Calculates the minimum time to revert a word to its initial state.
     * @param word The input word.
     * @param k The number of characters to remove from the beginning in each step.
     * @return The minimum number of steps required.
     */
    public int minimumTimeToInitialState(String word, int k) {
        int n = word.length();
        char[] s = word.toCharArray();
        int[] z = new int[n];
        int left = 0;
        int right = 0;

        for (int i = 1; i < n; i++) {
            if (i <= right) {
                z[i] = Math.min(right - i + 1, z[i - left]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > right) {
                left = i;
                right = i + z[i] - 1;
            }
        }

        for (int i = k; i < n; i += k) {
            if (z[i] == n - i) {
                return i / k;
            }
        }

        return (n + k - 1) / k;
    }
}