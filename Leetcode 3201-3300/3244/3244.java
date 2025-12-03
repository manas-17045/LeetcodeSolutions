// Leetcode 3244: Shortest Doistance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
// Solved on 3rd of November, 2025
class Solution {
    /**
     * Calculates the shortest distance after a series of road addition queries.
     * @param n The number of nodes in the graph.
     * @param queries A 2D array where each query `[u, v]` represents adding a road between node `u` and node `v`.
     * @return An array of integers, where each element is the shortest distance after the corresponding query.
     */
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        int distance = n - 1;
        int[] next = new int[n];
        for (int i = 0; i < n - 1; i++) {
            next[i] = i + 1;
        }

        int[] result = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];

            if (next[u] > 0 && next[u] < v) {
                int current = next[u];
                while (current < v) {
                    distance--;
                    int temp = next[current];
                    next[current] = 0;
                    current = temp;
                }
                next[u] = v;
            }
            result[i] = distance;
        }

        return result;
    }
}