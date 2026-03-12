// Leetcode 3600: 3600: Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
// Solved on 12th of March, 2026
class Solution {
    class DSU {
        int[] parent;
        int[] rank;

        public DSU(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        public int find(int i) {
            if (parent[i] == i) {
                return i;
            }
            return parent[i] = find(parent[i]);
        }

        public boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            
            if (rootI != rootJ) {
                if (rank[rootI] < rank[rootJ]) {
                    parent[rootI] = rootJ;
                } else if (rank[rootI] > rank[rootJ]) {
                    parent[rootJ] = rootI;
                } else {
                    parent[rootJ] = rootI;
                    rank[rootI]++;
                }
                return true;
            }
            return false;
        }
    }

    /**
     * Calculates the maximum stability achievable for a spanning tree given a set of edges and upgrade constraints.
     *
     * @param n     The number of nodes in the graph.
     * @param edges An array of edges where each edge is [u, v, strength, isMustInclude].
     * @param k     The maximum number of upgrades allowed (doubling the strength of an edge).
     * @return      The maximum possible minimum strength (stability) of the spanning tree, or -1 if no valid tree exists.
     */
    public int maxStability(int n, int[][] edges, int k) {
        DSU allEdgesDsu = new DSU(n);
        DSU mustEdgesDsu = new DSU(n);
        int totalComponents = n;
        int maxStrength = 0;
        int minMustStrength = Integer.MAX_VALUE;

        for (int[] edge : edges) {
            if (allEdgesDsu.union(edge[0], edge[1])) {
                totalComponents--;
            }
            if (edge[3] == 1) {
                if (!mustEdgesDsu.union(edge[0], edge[1])) {
                    return -1;
                }
                minMustStrength = Math.min(minMustStrength, edge[2]);
            }
            maxStrength = Math.max(maxStrength, edge[2]);
        }

        if (totalComponents > 1) {
            return -1;
        }

        int low = 1;
        int high = maxStrength * 2;
        if (minMustStrength != Integer.MAX_VALUE) {
            high = Math.min(high, minMustStrength);
        }

        int result = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canAchieve(n, edges, k, mid)) {
                result = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return result;
    }

    private boolean canAchieve(int n, int[][] edges, int k, int target) {
        DSU dsu = new DSU(n);
        int components = n;

        for (int[] edge : edges) {
            if (edge[3] == 1) {
                if (edge[2] < target) {
                    return false;
                }
                if (dsu.union(edge[0], edge[1])) {
                    components--;
                }
            }
        }

        for (int[] edge : edges) {
            if (edge[3] == 0 && edge[2] >= target) {
                if (dsu.union(edge[0], edge[1])) {
                    components--;
                }
            }
        }

        int upgradesUsed = 0;
        for (int[] edge : edges) {
            if (edge[3] == 0 && edge[2] < target && edge[2] * 2 >= target) {
                if (dsu.union(edge[0], edge[1])) {
                    components--;
                    upgradesUsed++;
                }
            }
        }

        return components == 1 && upgradesUsed <= k;
    }
}