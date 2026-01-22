// Leetcode 3812: Minimum Edge Toggles on a Tree
// https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/
// Solved on 22nd of January, 2026
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private List<Integer> result;
    private List<Integer>[] graph;
    private int[] diff;
    private int[][] edgeList;

    /**
     * Finds the minimum number of edge toggles required to transform the start state
     * of nodes to the target state in a tree. Each toggle on an edge flips the state
     * of both connected nodes.
     * @param n The number of nodes in the tree.
     * @param edges A 2D array where edges[i] = [u, v] represents an edge between nodes u and v.
     * @param start A binary string representing the initial state of each node.
     * @param target A binary string representing the target state of each node.
     * @return A list of indices of the edges that need to be toggled, or a list containing -1 if impossible.
     */
    public List<Integer> minimumFlips(int n, int[][] edges, String start, String target) {
        diff = new int[n];
        char[] s = start.toCharArray();
        char[] t = target.toCharArray();
        for (int i = 0; i < n; i++) {
            diff[i] = s[i] ^ t[i];
        }

        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < edges.length; i++) {
            graph[edges[i][0]].add(i);
            graph[edges[i][1]].add(i);
        }

        edgeList = edges;
        result = new ArrayList<>();

        dfs(0, -1);

        if (diff[0] != 0) {
            List<Integer> impossible = new ArrayList<>();
            impossible.add(-1);
            return impossible;
        }

        Collections.sort(result);
        return result;
    }

    private void dfs(int u, int p) {
        for (int idx : graph[u]) {
            int v = (edgeList[idx][0] == u) ? edgeList[idx][1] : edgeList[idx][0];
            if (v != p) {
                dfs(v, u);
                if (diff[v] == 1) {
                    result.add(idx);
                    diff[v] ^= 1;
                    diff[u] ^= 1;
                }
            }
        }
    }
}