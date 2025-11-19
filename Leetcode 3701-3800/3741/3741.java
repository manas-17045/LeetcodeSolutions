// Leetcode 3741: Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/
// Solved on 19th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum distance between three equal elements in an array.
     * The distance is defined as 2 * (index_of_third_occurrence - index_of_first_occurrence).
     * @param nums An array of integers.
     * @return The minimum distance found, or -1 if no three equal elements exist.
     */
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        int minDistance = Integer.MAX_VALUE;
        int[] firstIndex = new int[n + 1];
        int[] secondIndex = new int[n + 1];
        Arrays.fill(firstIndex, -1);
        Arrays.fill(secondIndex, -1);

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            if (firstIndex[val] == -1) {
                firstIndex[val] = i;
            } else if (secondIndex[val] == -1) {
                secondIndex[val] = i;
            } else {
                int distance = 2 * (i - firstIndex[val]);
                if (distance < minDistance) {
                    minDistance = distance;
                }
                firstIndex[val] = secondIndex[val];
                secondIndex[val] = i;
            }
        }

        if (minDistance == Integer.MAX_VALUE) {
            return -1;
        }
        return minDistance;
    }
}