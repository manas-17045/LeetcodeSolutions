// Leetcode 2911: Minimum Changes to Make K Semi-palindromes
// https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
// Solved on 11th of December, 2025
class Solution {
    /**
     * Given a string `s` and an integer `k`, find the minimum number of changes needed to divide `s` into `k` semi-palindromic substrings.
     * A string is semi-palindromic if it can be divided into `d` equal-length substrings, and each corresponding character in these substrings forms a palindrome.
     * @param s The input string.
     * @param k The number of semi-palindromic substrings to divide `s` into.
     * @return The minimum number of changes required.
     */
    public int minimumChanges(String s, int k) {
        int n = s.length();
        char[] charArray = s.toCharArray();

        int[][] divisors = new int[n + 1][];
        for (int len = 1; len <= n; len++) {
            int count = 0;
            for (int d = 1; d < len; d++) {
                if (len % d == 0) count++;
            }
            divisors[len] = new int[count];
            int idx = 0;
            for (int d = 1; d < len; d++) {
                if (len % d == 0) divisors[len][idx++] = d;
            }
        }

        int[][] minCost = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                minCost[i][j] = Integer.MAX_VALUE / 2;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int len = j - i + 1;
                for (int d : divisors[len]) {
                    int currentCost = 0;
                    for (int offset = 0; offset < d; offset++) {
                        int left = i + offset;
                        int right = i + len - d + offset;
                        while (left < right) {
                            if (charArray[left] != charArray[right]) {
                                currentCost++;
                            }
                            left += d;
                            right -= d;
                        }
                    }
                    if (currentCost < minCost[i][j]) {
                        minCost[i][j] = currentCost;
                    }
                }
            }
        }

        int[][] dp = new int[k + 1][n + 1];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE / 2;
            }
        }
        dp[0][0] = 0;

        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                for (int p = 0; p < j; p++) {
                    if (j - p < 2) continue;
                    if (dp[i - 1][p] != Integer.MAX_VALUE / 2 && minCost[p][j - 1] != Integer.MAX_VALUE / 2) {
                        int total = dp[i - 1][p] + minCost[p][j - 1];
                        if (total < dp[i][j]) {
                            dp[i][j] = total;
                        }
                    }
                }
            }
        }

        return dp[k][n];
    }
}