// Leetcode 1855: Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
// Solved on 25th of November, 2025
class Solution {
    /**
     * Finds the maximum distance between a pair of indices (i, j) such that i <= j, nums1[i] <= nums2[j],
     * and the distance j - i is maximized.
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @return The maximum distance between a valid pair of indices.
     */
    public int maxDistance(int[] nums1, int[] nums2) {
        int i = 0;
        int j = 0;
        int maxDistance = 0;
        int n = nums1.length;
        int m = nums2.length;

        while (i < n && j < m) {
            if (nums1[i] > nums2[j]) {
                i++;
            } else {
                maxDistance = Math.max(maxDistance, j - i);
                j++;
            }
        }
        return maxDistance;
    }
}