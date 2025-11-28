// Leetcode 1577: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
// Solved on 28th of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of "type 1" and "type 2" triplets.
     * A type 1 triplet is (i, j, k) such that nums1[i]^2 == nums2[j] * nums2[k].
     * A type 2 triplet is (i, j, k) such that nums2[i]^2 == nums1[j] * nums1[k].
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @return The total number of such triplets.
     */
    public int numTriplets(int[] nums1, int[] nums2) {
        return countTriplets(nums1, nums2) + countTriplets(nums2, nums1);
    }

    private int countTriplets(int[] arr1, int[] arr2) {
        int count = 0;
        for (int num : arr1) {
            long target = (long) num * num;
            Map<Integer, Integer> map = new HashMap<>();
            for (int val : arr2) {
                if (target % val == 0) {
                    long complement = target / val;
                    if (complement <= Integer.MAX_VALUE) {
                        count += map.getOrDefault((int) complement, 0);
                    }
                }
                map.put(val, map.getOrDefault(val, 0) + 1);
            }
        }
        return count;
    }
}