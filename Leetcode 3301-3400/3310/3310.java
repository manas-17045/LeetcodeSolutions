// Leetcode 3310: Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/
// Solved on 29th of October, 2025
import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    /**
     * Determines which methods remain after removing a "suspicious" method and all methods reachable from it.
     * @param n The total number of methods, labeled from 0 to n-1.
     * @param k The index of the initial suspicious method.
     * @param invocations A 2D array where each `invocation[i] = [u, v]` means method `u` invokes method `v`.
     * @return A list of integers representing the indices of the methods that are not suspicious and do not invoke any suspicious methods.
     */
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] invocation : invocations) {
            adj.get(invocation[0]).add(invocation[1]);
        }

        boolean[] suspicious = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();

        queue.add(k);
        suspicious[k] = true;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj.get(u)) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    queue.add(v);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) {
                for (int neighbor : adj.get(i)) {
                    if (suspicious[neighbor]) {
                        List<Integer> allMethods = new ArrayList<>();
                        for (int j = 0; j < n; j++) {
                            allMethods.add(j);
                        }
                        return allMethods;
                    }
                }
            }
        }

        List<Integer> remainingMethods = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) {
                remainingMethods.add(i);
            }
        }
        return remainingMethods;
    }
}