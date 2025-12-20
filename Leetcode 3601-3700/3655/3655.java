// Leetcode 3655: XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/
// Solved on 20th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Applies a series of multiplication queries to an array and then calculates the XOR sum of the modified array.
     * Queries can be of two types:
     * 1. Large step (k > sqrt(n)): Directly apply multiplication to elements at intervals of k.
     * 2. Small step (k <= sqrt(n)): Use a difference array-like approach to efficiently track multiplications.
     * @param nums The initial array of integers.
     * @param queries A 2D array where each query is [l, r, k, v], meaning multiply nums[i] by v for i from l to r with step k.
     * @return The XOR sum of the final modified array.
     */
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int mod = 1000000007;
        int n = nums.length;
        int b = (int) Math.sqrt(n);

        int[] totalMul = new int[n];
        for (int i = 0; i < n; i++) {
            totalMul[i] = 1;
        }

        int[][] smallSteps = new int[b + 1][n + b + 1];
        for (int i = 0; i <= b; i++) {
            Arrays.fill(smallSteps[i], 1);
        }

        for (int[] query : queries) {
            int l = query[0];
            int r = query[1];
            int k = query[2];
            int v = query[3];

            if (k > b) {
                for (int i = l; i <= r; i += k) {
                    totalMul[i] = (int) ((1L * totalMul[i] * v) % mod);
                }
            } else {
                int inv = power(v, mod - 2, mod);
                smallSteps[k][l] = (int) ((1L * smallSteps[k][l] * v) % mod);

                int steps = (r - l) / k;
                int nextIdx = l + (steps + 1) * k;

                if (nextIdx < smallSteps[k].length) {
                    smallSteps[k][nextIdx] = (int) ((1L * smallSteps[k][nextIdx] * inv) % mod);
                }
            }
        }

        for (int k = 1; k <= b; k++) {
            for (int i = 0; i < n; i++) {
                if (i >= k) {
                    smallSteps[k][i] = (int) ((1L * smallSteps[k][i] * smallSteps[k][i - k]) % mod);
                }
                totalMul[i] = (int) ((1L * totalMul[i] * smallSteps[k][i]) % mod);
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            long finalVal = (1L * nums[i] * totalMul[i]) % mod;
            result ^= (int) finalVal;
        }

        return result;
    }

    private int power(long base, int exp, int mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return (int) res;
    }
}