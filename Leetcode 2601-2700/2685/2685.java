// Leetcode 2685: Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/
// Solved on 11th of July, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Counts the number of complete components in a graph.
     * 
     * @param n The number of nodes in the graph.
     * @param edges The edges in the graph.
     * @return The number of complete components.
     */
    public int countCompleteComponents(int n, int[][] edges) {
        List<Integer>[] adjList = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            adjList[edge[0]].add(edge[1]);
            adjList[edge[1]].add(edge[0]);
        }
        boolean[] visited = new boolean[n];
        int completeComponents = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int[] stats = new int[2];
                dfs(i, adjList, visited, stats);
                if (stats[1] == stats[0] * (stats[0] - 1)) {
                    completeComponents++;
                }
            }
        }
        return completeComponents;
    }

    private void dfs(int node, List<Integer>[] adjList, boolean[] visited, int[] stats) {
        visited[node] = true;
        stats[0]++;
        stats[1] += adjList[node].size();
        for (int neighbor : adjList[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adjList, visited, stats);
            }
        }
    }
}