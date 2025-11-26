// Leetcode 3357: Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/
// Solved on 26th of November, 2025
class Solution {
    /**
     * Minimizes the maximum adjacent element difference by filling in -1s.
     * The goal is to replace each -1 with an integer such that the maximum absolute difference
     * between any two adjacent elements in the modified array is minimized.
     * @param nums The input array, possibly containing -1s.
     * @return The minimized maximum adjacent element difference.
     */
    public int minDifference(int[] nums) {
        int n = nums.length;
        int minDiff = 0;
        
        // Structures to capture segments of -1s
        // We use arrays to store segment data: 
        // segU[i], segV[i] are the boundary values. 
        // segLen[i] is the length of the -1 segment.
        // For head/tail segments, one boundary will be -1.
        int[] segU = new int[n];
        int[] segV = new int[n];
        int[] segLen = new int[n];
        int segCount = 0;
        
        int firstValIndex = -1;
        int lastValIndex = -1;
        
        // Calculate initial minDiff from existing adjacent pairs
        // and find boundaries of value range
        for (int i = 0; i < n; i++) {
            if (nums[i] != -1) {
                if (i + 1 < n && nums[i + 1] != -1) {
                    minDiff = Math.max(minDiff, Math.abs(nums[i] - nums[i + 1]));
                }
                if (firstValIndex == -1) {
                    firstValIndex = i;
                }
                lastValIndex = i;
            }
        }
        
        // Edge Case: All -1s
        if (firstValIndex == -1) return 0;
        
        // 1. Head Segment ( -1, -1, ... val )
        if (firstValIndex > 0) {
            segU[segCount] = nums[firstValIndex];
            segV[segCount] = -1; // -1 indicates boundary/infinity
            segLen[segCount] = firstValIndex;
            segCount++;
        }
        
        // 2. Internal Segments ( val, -1, -1, ... val )
        for (int i = firstValIndex; i < lastValIndex; ) {
            int j = i + 1;
            while (j < lastValIndex && nums[j] == -1) {
                j++;
            }
            // j is now the index of the next number
            if (j > i + 1) { // Found a gap of -1s
                segU[segCount] = nums[i];
                segV[segCount] = nums[j];
                segLen[segCount] = j - i - 1;
                segCount++;
            }
            i = j;
        }

        // 3. Tail Segment ( val, -1, -1 ... )
        if (lastValIndex < n - 1) {
            segU[segCount] = nums[lastValIndex];
            segV[segCount] = -1;
            segLen[segCount] = (n - 1) - lastValIndex;
            segCount++;
        }
        
        // Binary Search for the answer k
        int lo = minDiff, hi = 1000000000;
        int ans = hi;
        
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (check(mid, segU, segV, segLen, segCount)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }

    private boolean check(int k, int[] segU, int[] segV, int[] segLen, int segCount) {
        // We can succeed if EITHER:
        // 1. We can assign values such that each connected component of -1s is monochromatic (all X or all Y).
        //    This allows arbitrarily large distance between X and Y.
        if (solveDisjoint(k, segU, segV, segLen, segCount)) {
            return true;
        }
        
        // 2. We assign values allowing mixing X and Y within components.
        //    This REQUIRES |X - Y| <= k.
        if (solveMixed(k, segU, segV, segLen, segCount)) {
            return true;
        }
        
        return false;
    }
    
    // Check if valid assuming components are either all-X or all-Y
    private boolean solveDisjoint(int k, int[] segU, int[] segV, int[] segLen, int segCount) {
        long globalRMin = Long.MAX_VALUE;
        long globalLMax = Long.MIN_VALUE;
        
        // Temporary arrays to store constraints for the coverage check
        long[] L = new long[segCount];
        long[] R = new long[segCount];
        
        for (int i = 0; i < segCount; i++) {
            int u = segU[i];
            int v = segV[i];
            
            long l, r;
            if (v == -1) { // Single boundary (Head/Tail)
                l = (long)u - k;
                r = (long)u + k;
            } else { // Two boundaries (Gap)
                int minVal = Math.min(u, v);
                int maxVal = Math.max(u, v);
                // Constraint: All -1s in gap must be within k of BOTH u and v.
                // Intersection of [u-k, u+k] and [v-k, v+k]
                // equals [max(u,v)-k, min(u,v)+k]
                if ((long)maxVal - minVal > 2L * k) {
                    return false;   // Impossible to satisfy both
                }
                l = (long)maxVal - k;
                r = (long)minVal + k;
            }
            L[i] = l;
            R[i] = r;
            
            globalRMin = Math.min(globalRMin, r);
            globalLMax = Math.max(globalLMax, l);
        }
        
        // If one interval covers everything
        if (globalLMax <= globalRMin) {
            return true;
        }
        
        // Greedy: Pick X = globalRMin (optimal to cover left-ending intervals)
        long X = globalRMin;
        
        // Determine what Y must cover
        long yLMax = Long.MIN_VALUE;
        long yRMin = Long.MAX_VALUE;
        boolean needed = false;
        
        for (int i = 0; i < segCount; i++) {
            // If X does not cover interval i (L[i] > X)
            if (L[i] > X) {
                needed = true;
                yLMax = Math.max(yLMax, L[i]);
                yRMin = Math.min(yRMin, R[i]);
            }
        }
        
        if (!needed) return true; // X covered everything
        return yLMax <= yRMin; // Can Y cover the rest?
    }

    // Check if valid assuming |X - Y| <= k (allows mixing within components)
    private boolean solveMixed(int k, int[] segU, int[] segV, int[] segLen, int segCount) {
        long globalRMin = Long.MAX_VALUE;
        
        // Pass 1: Calculate globalRMin based on all individual constraints
        for (int i = 0; i < segCount; i++) {
            int u = segU[i];
            int v = segV[i];
            int len = segLen[i];
            
            if (v != -1 && len == 1) {
                // Single gap len 1: [max-k, min+k]
                int minVal = Math.min(u, v);
                int maxVal = Math.max(u, v);
                if ((long)maxVal - minVal > 2L * k) {
                    return false;
                }
                globalRMin = Math.min(globalRMin, (long)minVal + k);
            } else {
                // Gap > 1 or Edge: Individual constraints [u-k, u+k] etc.
                globalRMin = Math.min(globalRMin, (long)u + k);
                if (v != -1) {
                    globalRMin = Math.min(globalRMin, (long)v + k);
                }
            }
        }
        
        long X = globalRMin;
        
        long yLMax = Long.MIN_VALUE;
        long yRMin = Long.MAX_VALUE;
        boolean needed = false;
        
        // Pass 2: Identify leftovers for Y
        for (int i = 0; i < segCount; i++) {
            int u = segU[i];
            int v = segV[i];
            int len = segLen[i];
            
            if (v != -1 && len == 1) {
                long l = (long)Math.max(u, v) - k;
                long r = (long)Math.min(u, v) + k;
                if (X < l) {
                    needed = true;
                    yLMax = Math.max(yLMax, l);
                    yRMin = Math.min(yRMin, r);
                }
            } else {
                // Constraint from u
                long l1 = (long)u - k;
                long r1 = (long)u + k;
                if (X < l1) {
                    needed = true;
                    yLMax = Math.max(yLMax, l1);
                    yRMin = Math.min(yRMin, r1);
                }
                // Constraint from v (if exists)
                if (v != -1) {
                    long l2 = (long)v - k;
                    long r2 = (long)v + k;
                    if (X < l2) {
                        needed = true;
                        yLMax = Math.max(yLMax, l2);
                        yRMin = Math.min(yRMin, r2);
                    }
                }
            }
        }
        
        if (!needed) {
            return true;
        }
        if (yLMax > yRMin) {
            return false;
        }
        
        // Check if Y can be within k distance of X
        // We need Y in [yLMax, yRMin] AND Y in [X-k, X+k]
        long intersectL = Math.max(yLMax, X - k);
        long intersectR = Math.min(yRMin, X + k);
        
        return intersectL <= intersectR;
    }
}