// Leetcode 1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
// Solved on 10th of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
    class DSU {
        private int[] parent;
        private int count;

        public DSU(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
            count = n;
        }

        public int find(int i) {
            if (parent[i] == i) {
                return i;
            }
            parent[i] = find(parent[i]);
            return parent[i];
        }

        public boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI != rootJ) {
                parent[rootI] = rootJ;
                count--;
                return true;
            }
            return false;
        }

        public int getCount() {
            return count;
        }
    }

    /**
     * Finds critical and pseudo-critical edges in a Minimum Spanning Tree (MST).
     *
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where each inner array represents an edge [u, v, weight].
     * @return A list of two lists: the first list contains the indices of critical edges, and the second list contains the indices of pseudo-critical edges.
     */
    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges) {
        int e = edges.length;

        int[][] indexedEdges = new int[e][4];
        for (int i = 0; i < e; i++) {
            indexedEdges[i][0] = edges[i][0];
            indexedEdges[i][1] = edges[i][1];
            indexedEdges[i][2] = edges[i][2];
            indexedEdges[i][3] = i;
        }

        Arrays.sort(indexedEdges, Comparator.comparingInt(a -> a[2]));

        int minMstWeight = kruskal(n, indexedEdges, -1, -1);

        List<Integer> criticalEdges = new ArrayList<>();
        List<Integer> pseudoCriticalEdges = new ArrayList<>();

        for (int i = 0; i < e; i++) {
            int originalIndex = indexedEdges[i][3];

            int mstWithoutEdge = kruskal(n, indexedEdges, i, -1);

            if (mstWithoutEdge > minMstWeight) {
                criticalEdges.add(originalIndex);
                continue;
            }

            int mstWithEdge = kruskal(n, indexedEdges, -1, i);

            if (mstWithEdge == minMstWeight) {
                pseudoCriticalEdges.add(originalIndex);
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        result.add(criticalEdges);
        result.add(pseudoCriticalEdges);
        return result;
    }

    private int kruskal(int n, int[][] edges, int excludeIndex, int includeIndex) {
        DSU dsu = new DSU(n);
        int mstWeight = 0;
        int edgesUsed = 0;
        int maxPossibleWeight = 1001 * 200 + 1;

        if (includeIndex != -1) {
            int[] edge = edges[includeIndex];
            dsu.union(edge[0], edge[1]);
            mstWeight += edge[2];
            edgesUsed++;
        }

        for (int i = 0; i < edges.length; i++) {
            if (i == excludeIndex || i == includeIndex) {
                continue;
            }

            int[] edge = edges[i];
            if (dsu.union(edge[0], edge[1])) {
                mstWeight += edge[2];
                edgesUsed++;
            }
        }

        if (edgesUsed != n - 1) {
            return maxPossibleWeight;
        }

        return mstWeight;
    }
}