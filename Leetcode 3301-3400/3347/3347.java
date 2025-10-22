// Leetcode 3347: Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
// Solved on 22nd of October, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the maximum frequency of an element in the array after performing at most numOperations operations.
     * An operation consists of increasing an element by 1.
     *
     * @param nums A list of integers.
     * @param k The maximum allowed difference between elements in a valid window.
     * @param numOperations The maximum number of operations allowed.
     * @return The maximum possible frequency of an element.
     */
    public int maxFrequency(int[] nums, int k, int numOperations) {
        int n = nums.length;
        // diff map for intervals [nums[i]-k, nums[i]+k] using R+1 trick
        HashMap<Long, Integer> diff = new HashMap<>();
        // frequency of original values
        HashMap<Long, Integer> freq = new HashMap<>();
        
        for (int x : nums) {
            long L = (long)x - k;
            long R = (long)x + k;
            diff.put(L, diff.getOrDefault(L, 0) + 1);
            long R1 = R + 1;
            diff.put(R1, diff.getOrDefault(R1, 0) - 1);
            long xv = x;
            freq.put(xv, freq.getOrDefault(xv, 0) + 1);
        }
        
        // Sort keys of diff
        ArrayList<Long> keys = new ArrayList<>(diff.keySet());
        Collections.sort(keys);
        // Sort unique original values
        ArrayList<Long> origVals = new ArrayList<>(freq.keySet());
        Collections.sort(origVals);
        
        long currentCover = 0L;
        int idxOrig = 0;
        int res = 0;
        
        if (keys.size() == 0) {
            // No intervals (shouldn't happen since nums non-empty)
            for (int v : freq.values()) res = Math.max(res, v);
            return res;
        }
        
        long prev = keys.get(0);
        // Iterate through keys
        for (int i = 0; i < keys.size(); ++i) {
            long key = keys.get(i);
            long segStart = prev;
            long segEnd = key - 1; // inclusive
            
            if (segStart <= segEnd) {
                // positions in [segStart, segEnd] have coverage = currentCover
                // candidate if we pick a value that didn't appear in original nums:
                int candZero = (int)Math.min(numOperations, currentCover);
                if (candZero > res) res = candZero;
                // Process any original values that lie in this range
                while (idxOrig < origVals.size()) {
                    long ov = origVals.get(idxOrig);
                    if (ov < segStart) {
                        idxOrig++;
                        continue;
                    }
                    if (ov > segEnd) break;
                    int origCount = freq.get(ov);
                    int cand = (int)Math.min((long)origCount + (long)numOperations, currentCover);
                    if (cand > res) res = cand;
                    idxOrig++;
                }
            }
            // Apply diff at 'key' (affects positions >= key)
            currentCover += diff.getOrDefault(key, 0);
            prev = key;
        }
        // After loop, process remaining range [prev, +inf) with currentCover
        // only original values beyond or equal prev need processing (others already done)
        if (idxOrig < origVals.size()) {
            int candZero = (int)Math.min(numOperations, currentCover);
            if (candZero > res) res = candZero;
            while (idxOrig < origVals.size()) {
                long ov = origVals.get(idxOrig);
                int origCount = freq.get(ov);
                int cand = (int)Math.min((long)origCount + (long)numOperations, currentCover);
                if (cand > res) res = cand;
                idxOrig++;
            }
        } else {
            // Maybe no original values left but there is still a range where cover>0
            int candZero = (int)Math.min(numOperations, currentCover);
            if (candZero > res) res = candZero;
        }
        
        // Final answer cannot exceed n
        return Math.min(res, n);
    }
}