// Leetcode 2493: Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
// Solved on 10th of December, 2025
import java.util.*;

class Solution {
    /**
     * Divides nodes into the maximum number of groups such that no two adjacent nodes are in the same group,
     * and nodes in the same group are not adjacent.
     *
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where each inner array represents an edge [u, v].
     * @return The maximum number of groups, or -1 if it's impossible to divide the nodes.
     */
    public int magnificentSets(int n, int[][] edges) {
        // Build Adjacency List
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        int totalMaxGroups = 0;
        boolean[] visited = new boolean[n + 1];

        // Process each connected component
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                // Find all nodes in the current component
                List<Integer> componentNodes = new ArrayList<>();
                Queue<Integer> componentQueue = new LinkedList<>();
                componentQueue.offer(i);
                visited[i] = true;
                componentNodes.add(i);

                while (!componentQueue.isEmpty()) {
                    int u = componentQueue.poll();
                    for (int v : adj.get(u)) {
                        if (!visited[v]) {
                            visited[v] = true;
                            componentQueue.offer(v);
                            componentNodes.add(v);
                        }
                    }
                }

                // Calculate the max groups for this component
                int componentMaxGroups = 0;
                
                // For each component, try starting BFS from every node
                for (int startNode : componentNodes) {
                    int maxGroups = bfs(startNode, adj, n);
                    
                    if (maxGroups == -1) {
                        // Impossible grouping for this component (not bipartite)
                        return -1;
                    }
                    componentMaxGroups = Math.max(componentMaxGroups, maxGroups);
                }
                
                totalMaxGroups += componentMaxGroups;
            }
        }

        return totalMaxGroups;
    }

    // Helper function to perform BFS and check bipartiteness
    private int bfs(int startNode, List<List<Integer>> adj, int n) {
        int[] groups = new int[n + 1];
        Queue<Integer> queue = new LinkedList<>();
        int maxGroup = 0;

        queue.offer(startNode);
        groups[startNode] = 1;
        maxGroup = 1;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            int currentGroup = groups[u];

            for (int v : adj.get(u)) {
                if (groups[v] == 0) {
                    groups[v] = currentGroup + 1;
                    maxGroup = Math.max(maxGroup, groups[v]);
                    queue.offer(v);
                } else if (Math.abs(groups[v] - currentGroup) != 1) {
                    return -1; 
                }
            }
        }

        return maxGroup;
    }
}