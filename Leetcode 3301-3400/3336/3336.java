// Leetcode 3336: Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
// Solved on 14th of July, 2026
class Solution {
    /**
     * Counts the number of subsequences with equal GCD
     * 
     * @param nums array of integers
     * @return number of subsequences with equal GCD
     */
    public int subsequencePairCount(int[] nums) {
        int mod = 1000000007;
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        int[][] dp = new int[maxVal + 1][maxVal + 1];
        dp[0][0] = 1;
        for (int num : nums) {
            int[][] nextDp = new int[maxVal + 1][maxVal + 1];
            for (int i = 0; i <= maxVal; i++) {
                for (int j = 0; j <= maxVal; j++) {
                    if (dp[i][j] == 0) {
                        continue;
                    }
                    int val = dp[i][j];
                    nextDp[i][j] = (nextDp[i][j] + val) % mod;
                    int nextI = i == 0 ? num : gcd(i, num);
                    nextDp[nextI][j] = (nextDp[nextI][j] + val) % mod;
                    int nextJ = j == 0 ? num : gcd(j, num);
                    nextDp[i][nextJ] = (nextDp[i][nextJ] + val) % mod;
                }
            }
            dp = nextDp;
        }
        int result = 0;
        for (int k = 1; k <= maxVal; k++) {
            result = (result + dp[k][k]) % mod;
        }
        return result;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}