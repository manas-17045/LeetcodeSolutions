// Leetcode 3786: Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/
// Solved on 24th of December, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private long totalInteractionCost;
    private List<List<Integer>> adjacencyList;
    private int[][] subtreeGroupCounts;
    private int[] totalGroupCounts;
    private int[] nodeGroups;

    /**
     * Calculates the total sum of interaction costs in tree groups.
     * @param n The number of nodes in the tree.
     * @param edges An array of edges representing the tree structure.
     * @param group An array where group[i] is the group ID of node i.
     * @return The total sum of interaction costs.
     */
    public long interactionCosts(int n, int[][] edges, int[] group) {
        totalInteractionCost = 0;
        nodeGroups = group;
        
        adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            adjacencyList.get(edge[0]).add(edge[1]);
            adjacencyList.get(edge[1]).add(edge[0]);
        }

        totalGroupCounts = new int[22];
        for (int g : group) {
            totalGroupCounts[g]++;
        }

        subtreeGroupCounts = new int[n][22];
        dfs(0, -1);

        return totalInteractionCost;
    }

    private void dfs(int currentNode, int parentNode) {
        int currentGroup = nodeGroups[currentNode];
        subtreeGroupCounts[currentNode][currentGroup] = 1;

        for (int neighbor : adjacencyList.get(currentNode)) {
            if (neighbor == parentNode) {
                continue;
            }

            dfs(neighbor, currentNode);

            for (int i = 1; i <= 20; i++) {
                subtreeGroupCounts[currentNode][i] += subtreeGroupCounts[neighbor][i];
            }
        }

        if (parentNode != -1) {
            for (int i = 1; i <= 20; i++) {
                long countInSubtree = subtreeGroupCounts[currentNode][i];
                long countOutsideSubtree = totalGroupCounts[i] - countInSubtree;
                totalInteractionCost += countInSubtree * countOutsideSubtree;
            }
        }
    }
}