// Leetcode 960: Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
// Solved on 22nd of December, 2025
class Solution {
    /**
     * Given an array A of N strings, each of the same length,
     * we want to choose a subset of these columns so that after deleting the others,
     * the new table is sorted lexicographically, and the number of deleted columns is minimized.
     * @param strs The input array of strings.
     * @return The minimum number of columns that need to be deleted.
     */
    public int minDeletionSize(String[] strs) {
        int rowCount = strs.length;
        int colCount = strs[0].length();
        int[] dp = new int[colCount];
        int maxKept = 0;

        for (int i = 0; i < colCount; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                boolean canExtend = true;
                for (int k = 0; k < rowCount; k++) {
                    if (strs[k].charAt(j) > strs[k].charAt(i)) {
                        canExtend = false;
                        break;
                    }
                }
                if (canExtend) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxKept = Math.max(maxKept, dp[i]);
        }

        return colCount - maxKept;
    }
}