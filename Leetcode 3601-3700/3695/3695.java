// Leetcode 3695: Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/
// Solved on 23rd of November, 2025
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Calculates the maximum alternating sum of an array after performing a series of swaps.
     * Swaps can be performed between elements that are in the same connected component.
     * @param nums The input array of integers.
     * @param swaps A 2D array where each inner array `[a, b]` represents a possible swap between `nums[a]` and `nums[b]`.
     * @return The maximum possible alternating sum.
     */
    public long maxAlternatingSum(int[] nums, int[][] swaps) {
        int n = nums.length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int[] swap : swaps) {
            int rootA = find(parent, swap[0]);
            int rootB = find(parent, swap[1]);
            if (rootA != rootB) {
                parent[rootA] = rootB;
            }
        }

        List<Integer>[] components = new ArrayList[n];
        int[] evenCounts = new int[n];

        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            if (components[root] == null) {
                components[root] = new ArrayList<>();
            }
            components[root].add(nums[i]);
            if (i % 2 == 0) {
                evenCounts[root]++;
            }
        }

        long maxVal = 0;
        for (int i = 0; i < n; i++) {
            if (components[i] != null) {
                List<Integer> values = components[i];
                Collections.sort(values);
                
                int count = values.size();
                int evens = evenCounts[i];
                int odds = count - evens;

                for (int j = 0; j < count; j++) {
                    if (j < odds) {
                        maxVal -= values.get(j);
                    } else {
                        maxVal += values.get(j);
                    }
                }
            }
        }

        return maxVal;
    }

    private int find(int[] parent, int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent, parent[i]);
    }
}