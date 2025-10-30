// Leetcode 3132: Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/
// Solved on 30th of October, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds the minimum integer `x` such that `nums1` can be transformed into `nums2` by removing two elements from `nums1`
     * and adding `x` to all remaining elements.
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @return The minimum integer `x`.
     */
    public int minimumAddedInteger(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        int diff3 = nums2[0] - nums1[2];
        if (check(diff3, nums1, nums2)) {
            return diff3;
        }

        int diff2 = nums2[0] - nums1[1];
        if (check(diff2, nums1, nums2)) {
            return diff2;
        }

        return nums2[0] - nums1[0];
    }

    private boolean check(int x, int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int i = 0;
        int j = 0;
        int removed = 0;

        while (i < n) {
            if (j < m && (nums1[i] + x) == nums2[j]) {
                i++;
                j++;
            } else {
                removed++;
                i++;
            }
        }
        
        return removed == 2;
    }
}