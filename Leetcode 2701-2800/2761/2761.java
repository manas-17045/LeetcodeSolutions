// Leetcode 2761: Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/
// Solved on 25th of October, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Finds all pairs of prime numbers (x, y) such that x + y = n and x <= y.
     *
     * @param n The target sum.
     * @return A list of lists, where each inner list contains a pair of prime numbers [x, y].
     */
    public List<List<Integer>> findPrimePairs(int n) {
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);

        isPrime[0] = false;
        isPrime[1] = false;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>();

        if (n < 4) {
            return result;
        }

        for (int x = 2; x<= n / 2; x++) {
            int y = n - x;
            if (isPrime[x] && isPrime[y]) {
                result.add(Arrays.asList(x, y));
            }
        }

        return result;
    }
}