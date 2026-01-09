// Leetcode 3795: Minimum Subarrays Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/
// Solved on 9th of January, 2026
class Solution {
    /**
     * Given an array of positive integers nums and an integer k, return the minimum length of a subarray
     * such that the sum of its distinct elements is at least k. If no such subarray exists, return -1.
     * @param nums The input array of positive integers.
     * @param k The target sum for distinct elements.
     * @return The minimum length of a subarray with distinct sum at least k, or -1 if no such subarray exists.
     */
    public int minLength(int[] nums, int k) {
        long currentSum = 0;
        int minLen = Integer.MAX_VALUE;
        int left = 0;
        int[] counts = new int[100001];

        for (int right = 0; right < nums.length; right++) {
            if (counts[nums[right]] == 0) {
                currentSum += nums[right];
            }
            counts[nums[right]]++;

            while (currentSum >= k) {
                minLen = Math.min(minLen, right - left + 1);
                counts[nums[left]]--;
                if (counts[nums[left]] == 0) {
                    currentSum -= nums[left];
                }
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? -1 : minLen;
    }
}