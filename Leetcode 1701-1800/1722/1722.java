// Leetcode 1722: Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
// Solved on 21st of April, 2026
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the minimum Hamming distance between source and target arrays after any number of allowed swaps.
     *
     * @param source       The initial array of integers.
     * @param target       The target array of integers to compare against.
     * @param allowedSwaps An array of pairs representing indices that can be swapped.
     * @return The minimum possible Hamming distance between the modified source and the target.
     */
    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (int[] swap : allowedSwaps) {
            int rootA = find(parent, swap[0]);
            int rootB = find(parent, swap[1]);
            if (rootA != rootB) {
                parent[rootA] = rootB;
            }
        }
        Map<Integer, Integer>[] freqMaps = new HashMap[n];
        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            if (freqMaps[root] == null) {
                freqMaps[root] = new HashMap<>();
            }
            freqMaps[root].put(source[i], freqMaps[root].getOrDefault(source[i], 0) + 1);
        }
        int matches = 0;
        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            if (freqMaps[root] != null && freqMaps[root].getOrDefault(target[i], 0) > 0) {
                matches++;
                freqMaps[root].put(target[i], freqMaps[root].get(target[i]) - 1);
            }
        }
        return n - matches;
    }

    private int find(int[] parent, int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent, parent[i]);
    }
}