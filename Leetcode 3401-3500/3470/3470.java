// Leetcode 3470: Permutations IV
// https://leetcode.com/problems/permutations-iv/
// Solved on 15th of December, 2025
class Solution {
    long[][][] memo;
    long limit = 2000000000000000L;

    /**
     * Generates the k-th lexicographical permutation of numbers from 1 to n such that adjacent numbers have different parities.
     * @param n The upper limit of numbers to permute (1 to n).
     * @param k The 1-indexed rank of the desired permutation.
     * @return An array representing the k-th permutation, or an empty array if k is out of bounds.
     */
    public int[] permute(int n, long k) {
        memo = new long[n + 1][n + 1][2];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                java.util.Arrays.fill(memo[i][j], -1);
            }
        }

        int odds = (n + 1) / 2;
        long total = 0;
        
        for (int i = 1; i <= n; i++) {
            int remOdds = odds - (i % 2);
            long ways = count(n - 1, remOdds, i % 2);
            total += ways;
            if (total > limit) {
                total = limit;
                break;
            }
        }

        if (k > total) {
            return new int[0];
        }

        int[] result = new int[n];
        boolean[] used = new boolean[n + 1];

        for (int i = 0; i < n; i++) {
            for (int val = 1; val <= n; val++) {
                if (used[val]) {
                    continue;
                }
                
                if (i > 0 && (result[i - 1] % 2 == val % 2)) {
                    continue;
                }

                int remOdds = odds - (val % 2);
                long ways = count(n - 1 - i, remOdds, val % 2);

                if (k <= ways) {
                    result[i] = val;
                    used[val] = true;
                    if (val % 2 == 1) {
                        odds--;
                    }
                    break;
                } else {
                    k -= ways;
                }
            }
        }

        return result;
    }

    private long count(int len, int odds, int last) {
        if (len == 0) {
            return 1;
        }
        if (memo[len][odds][last] != -1) {
            return memo[len][odds][last];
        }

        long res = 0;
        if (last == 0) {
            if (odds > 0) {
                res = odds * count(len - 1, odds - 1, 1);
            }
        } else {
            int evens = len - odds;
            if (evens > 0) {
                res = evens * count(len - 1, odds, 0);
            }
        }

        if (res > limit) {
            res = limit;
        }
        return memo[len][odds][last] = res;
    }
}