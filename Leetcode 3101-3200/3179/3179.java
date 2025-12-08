// Leetcode 3179: Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-nth-value-after-k-seconds/
// Solved on 8th of December, 2025
class Solutio {
    /**
     * Calculates the value of the n-th element after k seconds.
     * @param n The number of elements.
     * @param k The number of seconds.
     * @return The value of the n-th element after k seconds, modulo 10^9 + 7.
     */
    public int valueAfterKSeconds(int n, int k) {
        int mod = 1000000007;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }
        for (int i = 0; i < k; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] = (dp[j] + dp[j - 1]) % mod;
            }
        }
        return dp[n - 1];
    }
}