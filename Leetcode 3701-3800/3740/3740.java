// Leetcode 3740: Minimum Distance Between Three EqualElements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/
// Solved on 10th of April, 2026
class Solution {
    /**
     * Calculates the minimum distance between three equal elements in the array.
     *
     * @param nums An array of integers.
     * @return The minimum distance found, or -1 if no three equal elements exist.
     */
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        int[] firstSeen = new int[n + 1];
        int[] secondSeen = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            firstSeen[i] = -1;
            secondSeen[i] = -1;
        }
        int minDistance = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (firstSeen[num] != -1) {
                int currentDistance = 2 * (i - firstSeen[num]);
                if (currentDistance < minDistance) {
                    minDistance = currentDistance;
                }
            }
            firstSeen[num] = secondSeen[num];
            secondSeen[num] = i;
        }
        if (minDistance == Integer.MAX_VALUE) {
            return -1;
        }
        return minDistance;
    }
}