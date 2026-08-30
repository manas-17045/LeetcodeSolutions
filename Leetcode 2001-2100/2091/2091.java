// Leetcode 2091: Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
// Solved on 30th of August, 2026
class Solution {
    /**
     * Calculates the minimum number of deletions required to remove both
     * the minimum and maximum elements from the array by deleting from
     * the front, the back, or both ends.
     *
     * @param nums the array of distinct integers
     * @return the minimum total deletions needed
     */
    public int minimumDeletions(int[] nums) {
        int n = nums.length;
        if (n <= 2) {
            return n;
        }

        int minIndex = 0;
        int maxIndex = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minIndex]) {
                minIndex = i;
            }
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }

        int firstIndex = Math.min(minIndex, maxIndex);
        int secondIndex = Math.max(minIndex, maxIndex);

        int removeFromFront = secondIndex + 1;
        int removeFromBack = n - firstIndex;
        int removeFromBoth = (firstIndex + 1) + (n - secondIndex);

        return Math.min(removeFromFront, Math.min(removeFromBack, removeFromBoth));
    }
}