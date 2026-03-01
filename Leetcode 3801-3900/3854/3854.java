// Leetcode 3854: Minimum Operations to Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/
// Solved on 1st of March, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum operations to make an array's parity alternate and the minimum 
     * range (max - min) of the resulting values.
     *
     * @param nums The input integer array.
     * @return An array containing [minimum operations, minimum difference].
     */
    public int[] makeParityAlternating(int[] nums) {
        int n = nums.length;
        int ops0 = 0;
        int ops1 = 0;
        for (int i = 0; i < n; i++) {
            int p = nums[i] % 2 == 0 ? 0 : 1;
            if (p != i % 2) {
                ops0++;
            }
            if (p != (1 - (i % 2))) {
                ops1++;
            }
        }
        
        int minOps = Math.min(ops0, ops1);
        int minDiff = Integer.MAX_VALUE;
        
        if (ops0 == minOps) {
            minDiff = Math.min(minDiff, solve(nums, 0));
        }
        if (ops1 == minOps) {
            minDiff = Math.min(minDiff, solve(nums, 1));
        }
        
        return new int[]{minOps, minDiff};
    }
    
    private int solve(int[] nums, int targetFirstParity) {
        int n = nums.length;
        int[][] vals = new int[n * 2][2];
        int size = 0;
        
        for (int i = 0; i < n; i++) {
            int p = nums[i] % 2 == 0 ? 0 : 1;
            int target = (targetFirstParity + i) % 2;
            if (p == target) {
                vals[size][0] = nums[i];
                vals[size][1] = i;
                size++;
            } else {
                vals[size][0] = nums[i] - 1;
                vals[size][1] = i;
                size++;
                vals[size][0] = nums[i] + 1;
                vals[size][1] = i;
                size++;
            }
        }
        
        Arrays.sort(vals, 0, size, (a, b) -> Integer.compare(a[0], b[0]));
        
        int[] counts = new int[n];
        int covered = 0;
        int minDiff = Integer.MAX_VALUE;
        int left = 0;
        
        for (int right = 0; right < size; right++) {
            int id = vals[right][1];
            if (counts[id] == 0) {
                covered++;
            }
            counts[id]++;
            
            while (covered == n) {
                minDiff = Math.min(minDiff, vals[right][0] - vals[left][0]);
                int leftId = vals[left][1];
                counts[leftId]--;
                if (counts[leftId] == 0) {
                    covered--;
                }
                left++;
            }
        }
        
        return minDiff;
    }
}