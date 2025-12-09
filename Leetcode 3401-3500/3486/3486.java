// Leetcode 3486: Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/
// Solved on 9th of December, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private int maxLen = -1;
    private int minNodes = 1;
    private List<int[]>[] adj;
    private int[] distMap;
    private List<Integer>[] valueHistory;

    /**
     * Finds the longest special path in a tree. A special path is defined by specific conditions
     * related to node values and path length.
     *
     * @param edges An array of edges where each edge is [u, v, weight].
     * @param nums An array where nums[i] is the value of node i.
     * @return An array of two integers: [maxLen, minNodes], representing the maximum length of a special path
     *         and the minimum number of nodes in such a path.
     */
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.length;
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[1], e[2]});
            adj[e[1]].add(new int[]{e[0], e[2]});
        }

        int maxVal = 0;
        for (int x : nums) {
            maxVal = Math.max(maxVal, x);
        }
        
        valueHistory = new ArrayList[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) {
            valueHistory[i] = new ArrayList<>();
        }
        
        distMap = new int[n];
        
        dfs(0, -1, 0, 0, 0, -1, nums);
        
        return new int[]{maxLen, minNodes};
    }

    private void dfs(int u, int p, int depth, int currentDist, int left, int dupStart, int[] nums) {
        int val = nums[u];
        distMap[depth] = currentDist;
        
        List<Integer> history = valueHistory[val];
        history.add(depth);
        int size = history.size();
        
        int nextLeft = left;
        int nextDupStart = dupStart;
        
        if (size >= 3) {
            int firstIdx = history.get(size - 3);
            nextLeft = Math.max(nextLeft, firstIdx + 1);
            if (nextDupStart < nextLeft) {
                nextDupStart = -1;
            }
        }
        
        if (size >= 2) {
            int pairStart = history.get(size - 2);
            if (pairStart >= nextLeft) {
                if (nextDupStart != -1 && nextDupStart != pairStart) {
                    nextLeft = Math.max(nextLeft, Math.min(nextDupStart, pairStart) + 1);
                    nextDupStart = Math.max(nextDupStart, pairStart);
                } else {
                    nextDupStart = pairStart;
                }
            }
        }
        
        int length = currentDist - distMap[nextLeft];
        int nodes = depth - nextLeft + 1;
        
        if (length > maxLen) {
            maxLen = length;
            minNodes = nodes;
        } else if (length == maxLen) {
            minNodes = Math.min(minNodes, nodes);
        }
        
        for (int[] e : adj[u]) {
            int v = e[0];
            int w = e[1];
            if (v != p) {
                dfs(v, u, depth + 1, currentDist + w, nextLeft, nextDupStart, nums);
            }
        }
        
        history.remove(size - 1);
    }
}