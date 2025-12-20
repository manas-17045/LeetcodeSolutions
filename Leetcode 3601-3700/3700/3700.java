// Leetcode 3700: Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/
// Solved on 20th of December, 2025
class Solution {
    /**
     * Calculates the number of "zigzag" arrays of length `n` where elements are chosen from the range `[l, r]`.
     * A zigzag array is defined as an array where elements strictly alternate between increasing and decreasing.
     * This version uses matrix exponentiation for potentially faster computation for large `n`.
     * @param n The length of the zigzag array.
     * @param l The lower bound of the range (inclusive).
     * @param r The upper bound of the range (inclusive).
     * @return The total number of zigzag arrays modulo 1,000,000,007.
     */
    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        long[] counts = new long[m];
        for (int i = 0; i < m; i++) {
            counts[i] = i;
        }

        long[][] transitionMatrix = new long[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if (j + i >= m) {
                    transitionMatrix[i][j] = 1;
                }
            }
        }

        long[][] poweredMatrix = power(transitionMatrix, n - 2);
        long[] finalCounts = multiplyVector(poweredMatrix, counts);

        long totalUp = 0;
        long mod = 1_000_000_007L;
        for (long count : finalCounts) {
            totalUp = (totalUp + count) % mod;
        }

        return (int) ((totalUp * 2) % mod);
    }

    private long[][] power(long[][] base, int exp) {
        int size = base.length;
        long[][] res = new long[size][size];
        for (int i = 0; i < size; i++) {
            res[i][i] = 1;
        }
        
        long[][] a = base;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = multiplyMatrix(res, a);
            }
            a = multiplyMatrix(a, a);
            exp >>= 1;
        }
        return res;
    }

    private long[][] multiplyMatrix(long[][] a, long[][] b) {
        int size = a.length;
        long[][] c = new long[size][size];
        long mod = 1_000_000_007L;
        for (int i = 0; i < size; i++) {
            for (int k = 0; k < size; k++) {
                if (a[i][k] == 0) {
                    continue;
                }
                for (int j = 0; j < size; j++) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod;
                }
            }
        }
        return c;
    }

    private long[] multiplyVector(long[][] matrix, long[] vec) {
        int size = matrix.length;
        long[] res = new long[size];
        long mod = 1_000_000_007L;
        for (int i = 0; i < size; i++) {
            long sum = 0;
            for (int j = 0; j < size; j++) {
                sum = (sum + matrix[i][j] * vec[j]) % mod;
            }
            res[i] = sum;
        }
        return res;
    }
}