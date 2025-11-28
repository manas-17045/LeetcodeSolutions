// Leetcode 3666: Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/
// Solved on 28th of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the minimum number of operations to equalize a binary string.
     * An operation consists of choosing a substring of length `k` and flipping all its bits.
     * The goal is to make all characters in the string the same ('0' or '1').
     *
     * @param s The input binary string.
     * @param k The length of the substring to flip in each operation.
     * @return The minimum number of operations, or -1 if it's impossible.
     */
    public int minOperations(String s, int k) {
        int n = s.length();
        int zeros = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                zeros++;
            }
        }

        if (zeros == 0) {
            return 0;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(zeros);

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        dist[zeros] = 0;

        TreeSet<Integer>[] unvisited = new TreeSet[2];
        for (int i = 0; i < 2; i++) {
            unvisited[i] = new TreeSet<>();
        }

        for (int i = 0; i <= n; i++) {
            if (i != zeros) {
                unvisited[i % 2].add(i);
            }
        }

        while (!queue.isEmpty()) {
            int u = queue.poll();
            int steps = dist[u];

            int minX = Math.max(0, k - (n - u));
            int maxX = Math.min(k, u);

            if (minX > maxX) {
                continue;
            }

            int minNext = u + k - 2 * maxX;
            int maxNext = u + k - 2 * minX;

            int targetParity = (u + k) % 2;

            NavigableSet<Integer> subSet = unvisited[targetParity].subSet(minNext, true, maxNext, true);
            Iterator<Integer> iterator = subSet.iterator();

            while (iterator.hasNext()) {
                int v = iterator.next();
                if (v == 0) {
                    return steps + 1;
                }
                dist[v] = steps + 1;
                queue.offer(v);
                iterator.remove();
            }
        }

        return -1;
    }
}