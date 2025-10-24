// Leetcode 3377: Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/
// Solved on 24th of October, 2025
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    private static final boolean[] isPrime = new boolean[10000];
    
    static {
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int p = 2; p * p < 10000; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i < 10000; i += p) {
                    isPrime[i] = false;
                }
            }
        }
    }

    /**
     * Calculates the minimum cost to transform integer n into integer m using digit operations.
     * @param n The starting integer.
     * @param m The target integer.
     * @return The minimum cost to transform n to m, or -1 if it's not possible or if n or m are prime.
     */
    public int minOperations(int n, int m) {
        if (isPrime[n] || isPrime[m]) {
            return -1;
        }

        long[] minCost = new long[10000];
        Arrays.fill(minCost, Long.MAX_VALUE);

        minCost[n] = n;
        
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.add(new long[]{(long)n, (long)n});

        while (!pq.isEmpty()) {
            long[] current = pq.poll();
            long cost = current[0];
            int u = (int)current[1];

            if (cost > minCost[u]) {
                continue;
            }

            if (u == m) {
                return (int)cost;
            }

            String uStr = String.valueOf(u);
            int numDigits = uStr.length();

            for (int i = 0; i < numDigits; i++) {
                int digit = uStr.charAt(i) - '0';
                
                long power = 1;
                for(int j = 0; j < numDigits - 1 - i; j++) {
                    power *= 10;
                }

                if (digit < 9) {
                    int v = u + (int)power;
                    if (!isPrime[v]) {
                        long newCost = cost + v;
                        if (newCost < minCost[v]) {
                            minCost[v] = newCost;
                            pq.add(new long[]{newCost, (long)v});
                        }
                    }
                }

                if (digit > 0) {
                    int v = u - (int)power;
                    if (!isPrime[v]) {
                        long newCost = cost + v;
                        if (newCost < minCost[v]) {
                            minCost[v] = newCost;
                            pq.add(new long[]{newCost, (long)v});
                        }
                    }
                }
            }
        }

        return -1;
    }
}