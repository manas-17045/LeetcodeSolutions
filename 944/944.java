// Leetcode 944: Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/
// Solved on 20th of December, 2025
class Solution {
    /**
     * Given an array A of N strings, each of the same length,
     * we want to choose a set of deletion indices D such that,
     * after deletions, the remaining columns are sorted lexicographically.
     * @param strs The input array of strings.
     * @return The number of columns that need to be deleted.
     */
    public int minDeletionSize(String[] strs) {
        int count = 0;
        int stringLength = strs[0].length();
        int arrayLength = strs.length;

        for (int col = 0; col < stringLength; col++) {
            for (int row = 0; row < arrayLength - 1; row++) {
                if (strs[row].charAt(col) > strs[row + 1].charAt(col)) {
                    count++;
                    break;
                }
            }
        }

        return count;
    }
}