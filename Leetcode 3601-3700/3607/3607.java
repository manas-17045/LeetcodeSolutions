// Leetcode 3607: Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/
// Solved on 6th of November, 2025
import java.util.*;

class Solution {
    /**
     * Processes a series of queries related to a power grid, determining the status of power stations.
     *
     * @param c The total number of power stations, labeled from 1 to c.
     * @param connections A 2D array representing initial connections between power stations.
     * @param queries A 2D array of queries. Each query is either [1, x] (check status of station x) or [2, x] (take station x offline).
     * @return An array of integers, where each element is the result of a type 1 query.
     */
    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        int n = c;
        int[] parent = new int[n + 1];
        int[] size = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        for (int[] e : connections) {
            int u = e[0];
            int v = e[1];
            union(parent, size, u, v);
        }
        TreeSet<Integer>[] sets = new TreeSet[n + 1];
        for (int i = 1; i <= n; i++) {
            int r = find(parent, i);
            if (sets[r] == null) {
                sets[r] = new TreeSet<>();
            }
            sets[r].add(i);
        }
        boolean[] online = new boolean[n + 1];
        Arrays.fill(online, true);
        int count = 0;
        for (int[] q : queries) {
            if (q[0] == 1) count++;
        }
        int[] result = new int[count];
        int idx = 0;
        for (int[] q : queries) {
            int type = q[0];
            int x = q[1];
            if (type == 1) {
                if (online[x]) {
                    result[idx++] = x;
                } else {
                    int r = find(parent, x);
                    TreeSet<Integer> set = sets[r];
                    if (set == null || set.isEmpty()) {
                        result[idx++] = -1;
                    } else {
                        result[idx++] = set.first();
                    }
                }
            } else {
                if (online[x]) {
                    online[x] = false;
                    int r = find(parent, x);
                    TreeSet<Integer> set = sets[r];
                    if (set != null) set.remove(x);
                }
            }
        }
        return result;
    }

    private int find(int[] parent, int x) {
        int root = x;
        while (parent[root] != root) root = parent[root];
        while (x != root) {
            int p = parent[x];
            parent[x] = root;
            x = p;
        }
        return root;
    }

    private void union(int[] parent, int[] size, int a, int b) {
        int ra = find(parent, a);
        int rb = find(parent, b);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            int tmp = ra;
            ra = rb;
            rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    }
}