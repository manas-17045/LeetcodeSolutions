// Leetcode 955: Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
// Solved on 21st of December, 2025
class Solution {
    /**
     * Given an array of N strings, each of length L, we are looking for the minimum number of columns to delete
     * such that the remaining columns are sorted lexicographically.
     * @param strs An array of strings.
     * @return The minimum number of columns that need to be deleted.
     */
    public int minDeletionSize(String[] strs) {
        int rows = strs.length;
        int cols = strs[0].length();
        int deleteCount = 0;
        boolean[] isSorted = new boolean[rows - 1];

        for (int j = 0; j < cols; j++) {
            boolean currentColumnInvalid = false;
            for (int i = 0; i < rows - 1; i++) {
                if (!isSorted[i] && strs[i].charAt(j) > strs[i + 1].charAt(j)) {
                    currentColumnInvalid = true;
                    break;
                }
            }

            if (currentColumnInvalid) {
                deleteCount++;
            } else {
                for (int i = 0; i < rows - 1; i++) {
                    if (strs[i].charAt(j) < strs[i + 1].charAt(j)) {
                        isSorted[i] = true;
                    }
                }
            }
        }
        
        return deleteCount;
    }
}