// Leetcode 2461: Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
// Solved on 31st of October, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the maximum sum of a subarray of length `k` where all elements in the subarray are distinct.
     * @param nums The input array of integers.
     * @param k The required length of the subarray.
     * @return The maximum sum of a distinct subarray of length `k`, or 0 if no such subarray exists.
     */
    public long maximumSubarraySum(int[] nums, int k) {
        long maxSum = 0;
        long currentSum = 0;
        Map<Integer, Integer> counts = new HashMap<>();
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            int num = nums[right];
            currentSum += num;
            counts.put(num, counts.getOrDefault(num, 0) + 1);

            if (right - left + 1 == k) {
                if (counts.size() == k) {
                    maxSum = Math.max(maxSum, currentSum);
                }
                
                int leftNum = nums[left];
                currentSum -= leftNum;
                counts.put(leftNum, counts.get(leftNum) - 1);
                if (counts.get(leftNum) == 0) {
                    counts.remove(leftNum);
                }
                left++;
            }
        }
        
        return maxSum;
    }
}