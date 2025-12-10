// Leetcode 2360: Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/
// Solved on 10th of December, 2025
class Solution {
    /**
     * Finds the length of the longest cycle in a directed graph.
     *
     * @param edges An array where edges[i] is the node that node i points to, or -1 if node i does not point to any node.
     * @return The length of the longest cycle in the graph, or -1 if no cycle exists.
     */
    public int longestCycle(int[] edges) {
        int n = edges.length;
        int[] visitTime = new int[n];
        int timer = 1;
        int maxCycle = -1;

        for (int i = 0; i < n; i++) {
            if (visitTime[i] > 0) {
                continue;
            }
            int startTime = timer;
            int currentNode = i;
            while (currentNode != -1 && visitTime[currentNode] == 0) {
                visitTime[currentNode] = timer++;
                currentNode = edges[currentNode];
            }
            if (currentNode != -1 && visitTime[currentNode] >= startTime) {
                maxCycle = Math.max(maxCycle, timer - visitTime[currentNode]);
            }
        }
        return maxCycle;
    }
}