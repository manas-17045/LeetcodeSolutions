// Leetcode 2540: Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/
// Solved on 19th of May, 2026
class Solution {
    /**
     * Finds the minimum common integer between two sorted arrays.
     * 
     * @param nums1 The first sorted integer array.
     * @param nums2 The second sorted integer array.
     * @return The smallest common integer, or -1 if no common integer exists.
     */
    public int getCommon(int[] nums1, int[] nums2) {
        int indexOne = 0;
        int indexTwo = 0;
        
        while (indexOne < nums1.length && indexTwo < nums2.length) {
            if (nums1[indexOne] == nums2[indexTwo]) {
                return nums1[indexOne];
            } else if (nums1[indexOne] < nums2[indexTwo]) {
                indexOne++;
            } else {
                indexTwo++;
            }
        }
        
        return -1;
    }
}