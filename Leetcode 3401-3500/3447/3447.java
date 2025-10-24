// Leetcode 3447: Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/
// Solved on 23rd of October, 2025
class Solution {
    /**
     * Assigns elements to groups based on divisibility constraints.
     * For each group `g` in `groups`, it finds the smallest index `j` from `elements`
     * such that `elements[j]` divides `g`. If no such element exists, -1 is assigned.
     * @param groups An array of integers representing the group values.
     * @param elements An array of integers representing the available elements.
     * @return An array of integers where `assigned[i]` is the smallest index `j` from `elements`
     *         such that `elements[j]` divides `groups[i]`, or -1 if no such element exists.
     */
    public int[] assignElements(int[] groups, int[] elements) {
        int n = groups.length;
        int m = elements.length;
        if (n == 0) return new int[0];
        if (m == 0) {
            int[] res = new int[n];
            for (int i = 0; i < n; i++) res[i] = -1;
            return res;
        }
        
        // Find maximum group value (we only need answers up to this)
        int maxGroup = 0;
        for (int g : groups) if (g > maxGroup) maxGroup = g;
        
        // minIndexForValue[v] = smallest index j such that elements[j] == v, or -1
        int[] minIndexForValue = new int[maxGroup + 1];
        for (int i = 0; i <= maxGroup; i++) minIndexForValue[i] = -1;
        for (int j = 0; j < m; j++) {
            int v = elements[j];
            // Ignore element values greater than maxGroup because they cannot divide any group <= maxGroup
            if (v <= maxGroup) {
                if (minIndexForValue[v] == -1 || j < minIndexForValue[v]) {
                    minIndexForValue[v] = j;
                }
            }
        }
        
        // bestIndexForValue[k] = smallest element-index of any element value that divides k
        final int INF = Integer.MAX_VALUE;
        int[] bestIndexForValue = new int[maxGroup + 1];
        for (int i = 0; i <= maxGroup; i++) bestIndexForValue[i] = INF;
        
        // For each present element value v, update all multiples k of v
        for (int v = 1; v <= maxGroup; v++) {
            int idx = minIndexForValue[v];
            if (idx == -1) continue;
            for (int k = v; k <= maxGroup; k += v) {
                if (idx < bestIndexForValue[k]) bestIndexForValue[k] = idx;
            }
        }
        
        //Build answer for each group
        int[] assigned = new int[n];
        for (int i = 0; i < n; i++) {
            int g = groups[i];
            int best = bestIndexForValue[g];
            assigned[i] = (best == INF) ? -1 : best;
        }
        return assigned;
    }
}