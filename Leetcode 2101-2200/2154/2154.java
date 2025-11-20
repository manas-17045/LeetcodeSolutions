// Leetcode 2508: Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/
// Solved on 20th of November, 2025
import java.util.*;

class Solution {
    /**
     * Determines if it's possible to make the degrees of all nodes in a graph even by adding at most two edges.
     *
     * @param n The number of nodes in the graph.
     * @param edges A list of existing edges, where each edge is represented as a list of two integers [u, v].
     * @return True if it's possible to make all node degrees even, false otherwise.
     */
    public boolean isPossible(int n, List<List<Integer>> edges) {
        List<Set<Integer>> adj = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            adj.add(new HashSet<>());
        }

        for (List<Integer> edge : edges) {
            adj.get(edge.get(0)).add(edge.get(1));
            adj.get(edge.get(1)).add(edge.get(0));
        }

        List<Integer> oddNodes = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (adj.get(i).size() % 2 != 0) {
                oddNodes.add(i);
            }
        }

        int count = oddNodes.size();
        if (count == 0) {
            return true;
        }

        if (count == 2) {
            int u = oddNodes.get(0);
            int v = oddNodes.get(1);

            if (!adj.get(u).contains(v)) {
                return true;
            }

            for (int i = 1; i <= n; i++) {
                if (i == u || i == v) {
                    continue;
                }
                if (!adj.get(u).contains(i) && !adj.get(v).contains(i)) {
                    return true;
                }
            }
            return false;
        }

        if (count == 4) {
            int a = oddNodes.get(0);
            int b = oddNodes.get(1);
            int c = oddNodes.get(2);
            int d = oddNodes.get(3);

            if (!adj.get(a).contains(b) && !adj.get(c).contains(d)) {
                return true;
            }
            if (!adj.get(a).contains(c) && !adj.get(b).contains(d)) {
                return true;
            }
            if (!adj.get(a).contains(d) && !adj.get(b).contains(c)) {
                return true;
            }

            return false;
        }

        return false;
    }
}