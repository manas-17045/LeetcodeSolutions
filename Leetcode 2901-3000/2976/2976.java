// Leetcode 2976: Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/
// Solved on 29th of January, 2026
class Solution {
    /**
     * Calculates the minimum cost to convert the source string to the target string.
     *
     * @param source The initial string.
     * @param target The target string.
     * @param original The array of source characters for transformations.
     * @param changed The array of target characters for transformations.
     * @param cost The array of costs for each transformation.
     * @return The minimum total cost to convert source to target, or -1 if impossible.
     */
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        long[][] minCosts = new long[26][26];
        long infinity = Integer.MAX_VALUE;

        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                minCosts[i][j] = infinity;
            }
            minCosts[i][i] = 0;
        }

        for (int i = 0; i < original.length; i++) {
            int from = original[i] - 'a';
            int to = changed[i] - 'a';
            minCosts[from][to] = Math.min(minCosts[from][to], cost[i]);
        }

        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    if (minCosts[i][k] < infinity && minCosts[k][j] < infinity) {
                        minCosts[i][j] = Math.min(minCosts[i][j], minCosts[i][k] + minCosts[k][j]);
                    }
                }
            }
        }

        long totalCost = 0;
        int n = source.length();
        for (int i = 0; i < n; i++) {
            int from = source.charAt(i) - 'a';
            int to = target.charAt(i) - 'a';
            if (minCosts[from][to] == infinity) {
                return -1;
            }
            totalCost += minCosts[from][to];
        }

        return totalCost;
    }
}