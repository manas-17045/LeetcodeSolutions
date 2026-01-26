// Leetcode 3820: Pythagorean Distance Nodes in a Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/
// Solved on 26th of January, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    /**
     * Counts the number of special nodes in a tree. A node is special if the distances
     * from it to three given nodes x, y, and z form a Pythagorean triple.
     *
     * @param n The number of nodes in the tree.
     * @param edges The edges of the tree.
     * @param x The first reference node.
     * @param y The second reference node.
     * @param z The third reference node.
     * @return The number of special nodes.
     */
    public int specialNodes(int n, int[][] edges, int x, int y, int z) {
        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }

        int[] distX = getDistances(n, adjacencyList, x);
        int[] distY = getDistances(n, adjacencyList, y);
        int[] distZ = getDistances(n, adjacencyList, z);

        int specialCount = 0;
        for (int i = 0; i < n; i++) {
            int a = distX[i];
            int b = distY[i];
            int c = distZ[i];

            int[] dists = {a, b, c};
            Arrays.sort(dists);

            if ((long) dists[0] * dists[0] + (long) dists[1] * dists[1] == (long) dists[2] * dists[2]) {
                specialCount++;
            }
        }

        return specialCount;
    }

    private int[] getDistances(int n, List<List<Integer>> graph, int startNode) {
        int[] distances = new int[n];
        Arrays.fill(distances, -1);
        
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(startNode);
        distances[startNode] = 0;

        while (!queue.isEmpty()) {
            int currentNode = queue.poll();
            
            for (int neighbor : graph.get(currentNode)) {
                if (distances[neighbor] == -1) {
                    distances[neighbor] = distances[currentNode] + 1;
                    queue.offer(neighbor);
                }
            }
        }
        return distances;
    }
}