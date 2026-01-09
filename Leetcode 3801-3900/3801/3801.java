// Leetcode 3801: Minimum Cost to Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/
// Solved on 9th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum cost to merge a given set of sorted lists into a single sorted list.
     * @param lists A 2D array where each inner array is a sorted list of integers.
     * @return The minimum total cost to merge all lists. The cost of merging two lists is defined as
     *         the sum of their combined length plus the absolute difference of their medians.
     */
    public long minMergeCost(int[][] lists) {
        int n = lists.length;
        int limit = 1 << n;
        
        int[][] mergedLists = new int[limit][];
        int[] medians = new int[limit];
        int[] lengths = new int[limit];
        long[] minCosts = new long[limit];
        
        Arrays.fill(minCosts, Long.MAX_VALUE);
        
        for (int mask = 1; mask < limit; mask++) {
            if (Integer.bitCount(mask) == 1) {
                int index = Integer.numberOfTrailingZeros(mask);
                mergedLists[mask] = lists[index];
                minCosts[mask] = 0;
            } else {
                int bit = mask & -mask;
                int prevMask = mask ^ bit;
                mergedLists[mask] = mergeArrays(mergedLists[bit], mergedLists[prevMask]);
            }
            
            lengths[mask] = mergedLists[mask].length;
            medians[mask] = mergedLists[mask][(lengths[mask] - 1) / 2];
        }
        
        for (int mask = 1; mask < limit; mask++) {
            if (Integer.bitCount(mask) == 1) continue;
            
            int lowestBit = mask & -mask;
            int remainingBits = mask ^ lowestBit;
            
            for (int s = remainingBits; s >= 0; s = (s - 1) & remainingBits) {
                int leftMask = s | lowestBit;
                int rightMask = mask ^ leftMask;
                
                if (rightMask == 0) {
                    if (s == 0) break;
                    continue;
                }
                
                long currentCost = minCosts[leftMask] + minCosts[rightMask] 
                                 + lengths[mask] 
                                 + Math.abs(medians[leftMask] - medians[rightMask]);
                
                if (currentCost < minCosts[mask]) {
                    minCosts[mask] = currentCost;
                }
                
                if (s == 0) break;
            }
        }
        
        return minCosts[limit - 1];
    }
    
    private int[] mergeArrays(int[] arr1, int[] arr2) {
        int len1 = arr1.length;
        int len2 = arr2.length;
        int[] merged = new int[len1 + len2];
        
        int i = 0, j = 0, k = 0;
        while (i < len1 && j < len2) {
            if (arr1[i] <= arr2[j]) {
                merged[k++] = arr1[i++];
            } else {
                merged[k++] = arr2[j++];
            }
        }
        while (i < len1) merged[k++] = arr1[i++];
        while (j < len2) merged[k++] = arr2[j++];
        
        return merged;
    }
}