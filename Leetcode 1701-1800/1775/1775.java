// Leetcode 1775: Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
// Solved on 5th of March, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to make the sum of two arrays equal.
     * @param nums1 The first integer array.
     * @param nums2 The second integer array.
     * @return The minimum number of operations, or -1 if it is impossible.
     */
    public int minOperations(int[] nums1, int[] nums) {
        int sum1 = 0;
        for (int num : nums1) {
            sum1 += num;
        }
        
        int sum2 = 0;
        for (int num : nums2) {
            sum2 += num;
        }
        
        if (sum1 == sum2) {
            return 0;
        }
        
        if (sum1 < sum2) {
            return minOperations(nums2, nums1);
        }
        
        if (nums1.length > nums2.length * 6) {
            return -1;
        }
        
        int diff = sum1 - sum2;
        int[] counts = new int[6];
        
        for (int num : nums1) {
            counts[num - 1]++;
        }
        for (int num : nums2) {
            counts[6 - num]++;
        }
        
        int ops = 0;
        for (int i = 5; i > 0; i--) {
            if (counts[i] == 0) {
                continue;
            }
            
            int maxDiff = counts[i] * i;
            if (diff <= maxDiff) {
                ops += (diff + i - 1) / i;
                return ops;
            }
            
            ops += counts[i];
            diff -= maxDiff;
        }
        
        return -1;
    }
}