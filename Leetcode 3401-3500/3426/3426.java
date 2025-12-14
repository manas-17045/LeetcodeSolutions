// Leetcode 3426: Manhattan Distances of All Arrangements of Pieces
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces-of-a-binary-grid/
// Solved on 14th of December, 2025
class Solution {
    private long mod = 1000000007;

    /**
     * Calculates the sum of Manhattan distances of all arrangements of k pieces on an m x n grid.
     * @param m The number of rows in the grid.
     * @param n The number of columns in the grid.
     * @param k The number of pieces to place on the grid.
     * @return The sum of Manhattan distances of all arrangements modulo 10^9 + 7.
     */
    public int distanceSum(int m, int n, int k) {
        long totalCells = (long) m * n;
        long[] fact = new long[(int) totalCells + 1];
        long[] inv = new long[(int) totalCells + 1];
        
        fact[0] = 1;
        for (int i = 1; i <= totalCells; i++) {
            fact[i] = (fact[i - 1] * i) % mod;
        }
        
        inv[(int) totalCells] = power(fact[(int) totalCells], mod - 2);
        for (int i = (int) totalCells - 1; i >= 0; i--) {
            inv[i] = (inv[i + 1] * (i + 1)) % mod;
        }
        
        long comb = nCr((int) totalCells - 2, k - 2, fact, inv);
        
        long rowSum = (long) m * m % mod;
        rowSum = (rowSum - 1 + mod) % mod;
        rowSum = rowSum * m % mod;
        rowSum = rowSum * power(6, mod - 2) % mod;
        long totalRowDist = rowSum * n % mod * n % mod;
        
        long colSum = (long) n * n % mod;
        colSum = (colSum - 1 + mod) % mod;
        colSum = colSum * n % mod;
        colSum = colSum * power(6, mod - 2) % mod;
        long totalColDist = colSum * m % mod * m % mod;
        
        long totalDist = (totalRowDist + totalColDist) % mod;
        
        return (int) (totalDist * comb % mod);
    }

    private long nCr(int n, int r, long[] fact, long[] inv) {
        if (r < 0 || r > n) {
            return 0;
        }
        return fact[n] * inv[r] % mod * inv[n - r] % mod;
    }

    private long power(long base, long exp) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
}