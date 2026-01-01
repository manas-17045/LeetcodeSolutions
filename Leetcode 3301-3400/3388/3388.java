// Leetcode 3388: Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/
// Solved on 1st of January, 2026
class Solution {
    /**
     * Counts the number of beautiful splits in the given array.
     *
     * @param nums The input array of integers.
     * @return The number of beautiful splits.
     */
    public int beautifulSplits(int[] nums) {
        int n = nums.length;
        int count = 0;

        int[] z = new int[n];
        for (int i = 1; i < n; i++) {
            int len = 0;
            while (i + len < n && nums[len] == nums[i + len]) {
                len++;
            }
            z[i] = len;
        }

        int[] nextLcp = new int[n + 1];
        int[] currLcp = new int[n + 1];

        for (int i = n - 2; i >= 1; i--) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j]) {
                    currLcp[j] = 1 + nextLcp[j + 1];
                } else {
                    currLcp[j] = 0;
                }
            }

            for (int j = i + 1; j < n; j++) {
                boolean isBeautiful = false;

                if (i <= j - i && z[i] >= i) {
                    isBeautiful = true;
                }

                if (!isBeautiful && j - i <= n - j && currLcp[j] >= j - i) {
                    isBeautiful = true;
                }

                if (isBeautiful) {
                    count++;
                }
            }

            int[] temp = nextLcp;
            nextLcp = currLcp;
            currLcp = temp;
        }

        return count;
    }
}