// Leetcode 3900: Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/
// Solved on 27th of April, 2026
class Solution {
    /**
     * Calculates the length of the longest balanced substring possible after at most one swap.
     * 
     * @param s The input string consisting of '0's and '1's.
     * @return The length of the longest balanced substring.
     */
    public int longestBalanced(String s) {
        int n = s.length();
        int total0 = 0;
        int total1 = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                total0++;
            } else {
                total1++;
            }
        }
        
        int m = 2 * Math.min(total0, total1);
        if (m == 0) {
            return 0;
        }
        
        int[] f = new int[n + 1];
        for (int i = 0; i < n; i++) {
            f[i + 1] = f[i] + (s.charAt(i) == '1' ? 1 : -1);
        }
        
        int maxOffset = 2 * n + 3;
        int[] count = new int[maxOffset];
        for (int i = 0; i <= n; i++) {
            count[f[i] + n]++;
        }
        
        int[][] pos = new int[maxOffset][];
        for (int i = 0; i < maxOffset; i++) {
            if (count[i] > 0) {
                pos[i] = new int[count[i]];
            }
        }
        
        int[] idx = new int[maxOffset];
        for (int i = 0; i <= n; i++) {
            int v = f[i] + n;
            pos[v][idx[v]++] = i;
        }
        
        int[] ptr = new int[maxOffset];
        int maxLen = 0;
        int[] diffs = {-2, 0, 2};
        
        for (int j = 1; j <= n; j++) {
            for (int d : diffs) {
                int v = f[j] - d + n;
                if (v >= 0 && v < maxOffset) {
                    int[] list = pos[v];
                    if (list != null) {
                        while (ptr[v] < list.length && list[ptr[v]] < j - m) {
                            ptr[v]++;
                        }
                        if (ptr[v] < list.length) {
                            int i = list[ptr[v]];
                            if (i < j) {
                                if (j - i > maxLen) {
                                    maxLen = j - i;
                                }
                            }
                        }
                    }
                }
            }
        }
        
        return maxLen;
    }
}