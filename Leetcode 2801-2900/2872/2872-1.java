// Leetcode 2872: Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/
// Solved on 28th of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private int count;

    /**
     * Calculates the maximum number of k-divisible components in a tree.
     * A component is k-divisible if the sum of values of its nodes is divisible by k.
     *
     * @param n The number of nodes in the tree.
     * @param edges An array of edges representing the tree structure.
     * @param values An array where values[i] is the value of the i-th node.
     * @param k The divisor.
     * @return The maximum number of k-divisible components.
     */
    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        
        count = 0;
        dfs(0, -1, adj, values, k);
        return count;
    }

    private long dfs(int node, int parent, List<List<Integer>> adj, int[] values, int k) {
        long sum = values[node];
        for (int neighbor : adj.get(node)) {
            if (neighbor != parent) {
                sum += dfs(neighbor, node, adj, values, k);
            }
        }
        
        if (sum % k == 0) {
            count++;
            return 0;
        }
        return sum;
    }
}