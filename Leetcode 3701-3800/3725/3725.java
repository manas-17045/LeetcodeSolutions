// Leetcode 3725: Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-integers-from-rows/
// Solved on 6th of December, 2025
class Solution {
    /**
     * Counts the number of ways to choose one integer from each row of a given matrix such that their greatest common divisor (GCD) is 1.
     *
     * @param mat The input matrix of integers.
     * @return The number of ways to choose coprime integers from rows, modulo 10^9 + 7.
     */
    public int countCoprime(int[][] mat) {
        int mod = 1000000007;
        int limit = 150;
        long[] dp = new long[limit + 1];

        for (int num : mat[0]) {
            dp[num]++;
        }

        for (int i = 1; i < mat.length; i++) {
            long[] nextDp = new long[limit + 1];
            int[] count = new int[limit + 1];

            for (int num : mat[i]) {
                count[num]++;
            }

            for (int g = 1; g <= limit; g++) {
                if (dp[g] == 0) {
                    continue;
                }
                for (int v = 1; v <= limit; v++) {
                    if (count[v] == 0) {
                        continue;
                    }
                    int newGcd = gcd(g, v);
                    long ways = (dp[g] * count[v]) % mod;
                    nextDp[newGcd] = (nextDp[newGcd] + ways) % mod;
                }
            }
            dp = nextDp;
        }

        return (int) dp[1];
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