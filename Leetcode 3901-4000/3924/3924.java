// Leetcode 3924: Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/
// Solved on 23rd of May, 2026
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

class Solution {
    /**
     * Finds the minimum threshold such that there exists a path from source to target 
     * with at most k edges having a weight greater than the threshold.
     *
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where edges[i] = [u, v, weight] represents an undirected edge.
     * @param source The starting node.
     * @param target The destination node.
     * @param k The maximum allowed number of "heavy" edges (weight > threshold).
     * @return The minimum possible threshold, or -1 if no path exists.
     */
    public int minimumThreshold(int n, int[][] edges, int source, int target, int k) {
        List<List<int[]>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            adjList.get(u).add(new int[]{v, weight});
            adjList.get(v).add(new int[]{u, weight});
        }
        
        int lowThreshold = 0;
        int highThreshold = 1000000000;
        int minThreshold = -1;
        
        while (lowThreshold <= highThreshold) {
            int midThreshold = lowThreshold + (highThreshold - lowThreshold) / 2;
            if (hasValidPath(n, adjList, source, target, k, midThreshold)) {
                minThreshold = midThreshold;
                highThreshold = midThreshold - 1;
            } else {
                lowThreshold = midThreshold + 1;
            }
        }
        
        return minThreshold;
    }

    private boolean hasValidPath(int n, List<List<int[]>> adjList, int source, int target, int k, int threshold) {
        int[] distances = new int[n];
        Arrays.fill(distances, Integer.MAX_VALUE);
        Deque<Integer> deque = new ArrayDeque<>();
        
        distances[source] = 0;
        deque.offerFirst(source);
        
        while (!deque.isEmpty()) {
            int currentNode = deque.pollFirst();
            
            if (currentNode == target) {
                return distances[currentNode] <= k;
            }
            
            for (int[] neighbor : adjList.get(currentNode)) {
                int nextNode = neighbor[0];
                int edgeWeight = neighbor[1];
                int pathCost = edgeWeight <= threshold ? 0 : 1;
                
                if (distances[currentNode] + pathCost < distances[nextNode]) {
                    distances[nextNode] = distances[currentNode] + pathCost;
                    if (pathCost == 0) {
                        deque.offerFirst(nextNode);
                    } else {
                        deque.offerLast(nextNode);
                    }
                }
            }
        }
        
        return false;
    }
}