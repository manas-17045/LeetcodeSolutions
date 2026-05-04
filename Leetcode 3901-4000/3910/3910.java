// Leetcode 3910: Count Connected Subgraphs with Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/
// Solved on 4th of May, 2026
class Solution {
    /**
     * Counts the number of connected subgraphs where the sum of node values is even.
     *
     * @param nums An array of integers representing node values (0 or 1).
     * @param edges A 2D array representing the undirected edges of the graph.
     * @return The total count of connected subgraphs with an even sum.
     */
    public int evenSumSubgraphs(int[] nums, int[][] edges) {
        int n = nums.length;
        int[] adj = new int[n];
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            adj[u] |= (1 << v);
            adj[v] |= (1 << u);
        }
        
        int oddNodesMask = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                oddNodesMask |= (1 << i);
            }
        }
        
        int validSubgraphs = 0;
        int totalMasks = 1 << n;
        
        for (int mask = 1; mask < totalMasks; mask++) {
            if (Integer.bitCount(mask & oddNodesMask) % 2 != 0) {
                continue;
            }
            
            int startNode = Integer.numberOfTrailingZeros(mask);
            int visited = 1 << startNode;
            int queueMask = 1 << startNode;
            
            while (queueMask != 0) {
                int node = Integer.numberOfTrailingZeros(queueMask);
                queueMask &= ~(1 << node);
                
                int unvisitedNeighbors = (adj[node] & mask) & ~visited;
                visited |= unvisitedNeighbors;
                queueMask |= unvisitedNeighbors;
            }
            
            if (visited == mask) {
                validSubgraphs++;
            }
        }
        
        return validSubgraphs;
    }
}