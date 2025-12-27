// Leetcode 3732: Maximum Product of three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/
// Solved on 27th of December, 2025
class Solution {
    /**
     * Calculates the maximum product of three elements after one replacement.
     *
     * @param nums The input array of integers.
     * @return The maximum product of three elements after one replacement.
     */
    public long maxProduct(int[] nums) {
        long[] maxValues = {Long.MIN_VALUE, Long.MIN_VALUE, Long.MIN_VALUE};
        int[] maxIndices = {-1, -1, -1};
        long[] minValues = {Long.MAX_VALUE, Long.MAX_VALUE, Long.MAX_VALUE};
        int[] minIndices = {-1, -1, -1};
        
        for (int i = 0; i < nums.length; i++) {
            long val = nums[i];
            
            if (val > maxValues[0]) {
                maxValues[2] = maxValues[1];
                maxIndices[2] = maxIndices[1];
                maxValues[1] = maxValues[0];
                maxIndices[1] = maxIndices[0];
                maxValues[0] = val;
                maxIndices[0] = i;
            } else if (val > maxValues[1]) {
                maxValues[2] = maxValues[1];
                maxIndices[2] = maxIndices[1];
                maxValues[1] = val;
                maxIndices[1] = i;
            } else if (val > maxValues[2]) {
                maxValues[2] = val;
                maxIndices[2] = i;
            }
            
            if (val < minValues[0]) {
                minValues[2] = minValues[1];
                minIndices[2] = minIndices[1];
                minValues[1] = minValues[0];
                minIndices[1] = minIndices[0];
                minValues[0] = val;
                minIndices[0] = i;
            } else if (val < minValues[1]) {
                minValues[2] = minValues[1];
                minIndices[2] = minIndices[1];
                minValues[1] = val;
                minIndices[1] = i;
            } else if (val < minValues[2]) {
                minValues[2] = val;
                minIndices[2] = i;
            }
        }
        
        long maxProduct = Long.MIN_VALUE;
        long k = 100000;
        
        for (int i = 0; i < nums.length; i++) {
            long currentMax1, currentMax2;
            if (i == maxIndices[0]) {
                currentMax1 = maxValues[1];
                currentMax2 = maxValues[2];
            } else if (i == maxIndices[1]) {
                currentMax1 = maxValues[0];
                currentMax2 = maxValues[2];
            } else {
                currentMax1 = maxValues[0];
                currentMax2 = maxValues[1];
            }
            
            long currentMin1, currentMin2;
            if (i == minIndices[0]) {
                currentMin1 = minValues[1];
                currentMin2 = minValues[2];
            } else if (i == minIndices[1]) {
                currentMin1 = minValues[0];
                currentMin2 = minValues[2];
            } else {
                currentMin1 = minValues[0];
                currentMin2 = minValues[1];
            }
            
            long p1 = k * currentMax1 * currentMax2;
            long p2 = k * currentMin1 * currentMin2;
            long p3 = -k * currentMax1 * currentMin1;
            
            long currentBest = Math.max(p1, Math.max(p2, p3));
            if (currentBest > maxProduct) {
                maxProduct = currentBest;
            }
        }
        
        return maxProduct;
    }
}