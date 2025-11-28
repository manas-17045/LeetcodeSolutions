// Leetcode 2872: Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/
// Solved on 28th of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private int componentCount;

    /**
     * Calculates the maximum number of k-divisible components in a tree.
     * A component is k-divisible if the sum of values of its nodes is divisible by k.
     * @param n The number of nodes in the tree.
     * @param edges An array of edges representing the tree structure.
     * @param values An array where values[i] is the value of the i-th node.
     * @param k The divisor.
     * @return The maximum number of k-divisible components.
     */
    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        componentCount = 0;
        List<List<Integer>> adjacencyList = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }
        
        postOrderTraversal(0, -1, adjacencyList, values, k);
        
        return componentCount;
    }

    private long postOrderTraversal(int currentNode, int parentNode, List<List<Integer>> adjacencyList, int[] values, int k) {
        long currentSum = values[currentNode];
        
        for (int neighbor : adjacencyList.get(currentNode)) {
            if (neighbor != parentNode) {
                currentSum += postOrderTraversal(neighbor, currentNode, adjacencyList, values, k);
            }
        }
        
        if (currentSum % k == 0) {
            componentCount++;
            return 0;
        }
        
        return currentSum;
    }
}