// Leetcode 1411: Number of Ways to Paint N × 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
// Solved on 3rd of January, 2026
class Solution {
    /**
     * Calculates the number of ways to paint an n x 3 grid such that no two adjacent cells have the same color.
     * @param n The number of rows in the grid.
     * @return The number of ways to paint the grid, modulo 10^9 + 7.
     */
    public int numOfWays(int n) {
        long aba = 6;
        long abc = 6;
        long mod = 1000000007;

        for (int i = 1; i < n; i++) {
            long nextAba = (3 * aba + 2 * abc) % mod;
            long nextAbc = (2 * (aba + abc)) % mod;
            aba = nextAba;
            abc = nextAbc;
        }

        return (int) ((aba + abc) % mod);
    }
}