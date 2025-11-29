// Leetcode 3690: Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/
// Solved on 29th of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the minimum number of moves required to transform `nums1` into `nums2`
     * by repeatedly splitting a subarray and merging it back into a different position.
     * @param nums1 The initial array of integers.
     * @param nums2 The target array of integers.
     * @return The minimum number of moves, or -1 if `nums2` is unreachable.
     */
    public int minSplitMerge(int[] nums1, int[] nums2) {
        if (Arrays.equals(nums1, nums2)) {
            return 0;
        }

        int n = nums1.length;
        String target = Arrays.toString(nums2);
        
        Queue<int[]> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        
        queue.offer(nums1);
        visited.add(Arrays.toString(nums1));
        
        int moves = 0;
        
        while (!queue.isEmpty()) {
            moves++;
            int size = queue.size();
            
            for (int s = 0; s < size; s++) {
                int[] current = queue.poll();
                
                for (int i = 0; i < n; i++) {
                    for (int j = i; j < n; j++) {
                        int[] remainder = new int[n - (j - i + 1)];
                        int rIdx = 0;
                        for (int k = 0; k < n; k++) {
                            if (k < i || k > j) {
                                remainder[rIdx++] = current[k];
                            }
                        }
                        
                        for (int k = 0; k <= remainder.length; k++) {
                            if (k == i) continue;
                            
                            int[] next = new int[n];
                            int nIdx = 0;
                            
                            for (int p = 0; p < k; p++) {
                                next[nIdx++] = remainder[p];
                            }
                            
                            for (int p = i; p <= j; p++) {
                                next[nIdx++] = current[p];
                            }
                            
                            for (int p = k; p < remainder.length; p++) {
                                next[nIdx++] = remainder[p];
                            }
                            
                            String nextStr = Arrays.toString(next);
                            if (nextStr.equals(target)) {
                                return moves;
                            }
                            
                            if (visited.add(nextStr)) {
                                queue.offer(next);
                            }
                        }
                    }
                }
            }
        }
        
        return -1;
    }
}