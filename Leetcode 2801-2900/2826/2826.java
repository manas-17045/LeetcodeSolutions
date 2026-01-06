// Leetcode 2826: Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/
// Solved on 6th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to sort the given array into three groups.
     * An operation consists of changing an element's value.
     * The three groups must be non-decreasing, i.e., all 1s, then all 2s, then all 3s.
     * @param nums The input list of integers (each element is 1, 2, or 3).
     * @return The minimum number of operations.
     */
    public int minimumOperations(List<Integer> nums) {
        int len1 = 0;
        int len2 = 0;
        int len3 = 0;

        for (int num : nums) {
            if (num == 1) {
                len1++;
            } else if (num == 2) {
                len2++;
            } else {
                len3++;
            }
            len2 = Math.max(len2, len1);
            len3 = Math.max(len3, len2);
        }

        return nums.size() - len3;
    }
}