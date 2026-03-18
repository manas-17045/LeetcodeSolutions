// Leetcode 3868: Minimum Cost to Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/
// Solved on 18th of March, 2026
class Solution {
    /**
     * Calculates the minimum cost to equalize two arrays using swaps.
     * 
     * @param nums1 The first integer array.
     * @param nums2 The second integer array.
     * @return The minimum number of swaps required, or -1 if equalization is impossible.
     */
    public int minCost(int[] nums1, int[] nums2) {
        int maxVal = 0;
        for (int num : nums1) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        for (int num : nums2) {
            if (num > maxVal) {
                maxVal = num;
            }
        }

        int[] diff = new int[maxVal + 1];
        for (int i = 0; i < nums1.length; i++) {
            diff[nums1[i]]++;
            diff[nums2[i]]--;
        }

        int cost = 0;
        for (int count : diff) {
            if (count % 2 != 0) {
                return -1;
            }
            if (count > 0) {
                cost += count / 2;
            }
        }

        return cost;
    }
}