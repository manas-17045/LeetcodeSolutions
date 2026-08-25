// Leetcode 3718: Smallest Missing Multple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/
// Solved on 25th of August, 2026
class Solution {
    /**
     * Finds the smallest positive multiple of k missing from the array.
     *
     * @param nums the input array of positive integers
     * @param k the integer whose multiples are checked
     * @return the smallest positive multiple of k not present in nums
     */
    public int missingMultiple(int[] nums, int k) {
        boolean[] present = new boolean[101];
        for (int num : nums) {
            present[num] = true;
        }

        int multiple = k;
        while (multiple <= 100 && present[multiple]) {
            multiple += k;
        }

        return multiple;
    }
}