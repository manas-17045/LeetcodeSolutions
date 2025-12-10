// Leetcode 2608: Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/
// Solved on 10th of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    /**
     * Finds the length of the shortest cycle in an undirected graph.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where each inner array represents an edge [u, v].
     * @return The length of the shortest cycle, or -1 if no cycle exists.
     */
    public int findShortestCycle(int n, int[][] edges) {
        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adjacencyList.get(u).add(v);
            adjacencyList.get(v).add(u);
        }

        int minCycleLength = Integer.MAX_VALUE;

        for (int startNode = 0; startNode < n; startNode++) {
            int[] distance = new int[n];
            Arrays.fill(distance, -1);
            int[] parent = new int[n];
            Arrays.fill(parent, -1);
            
            Queue<Integer> queue = new LinkedList<>();

            distance[startNode] = 0;
            queue.offer(startNode);

            while (!queue.isEmpty()) {
                int u = queue.poll();

                for (int v : adjacencyList.get(u)) {
                    if (distance[v] == -1) {
                        distance[v] = distance[u] + 1;
                        parent[v] = u;
                        queue.offer(v);
                    } else if (v != parent[u]) {
                        int currentCycleLength = distance[u] + distance[v] + 1;
                        minCycleLength = Math.min(minCycleLength, currentCycleLength);
                    }
                }
            }
        }

        return (minCycleLength == Integer.MAX_VALUE) ? -1 : minCycleLength;
    }
}