// Leetcode 3489: Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/
// Solved on 21st of November, 2025
class Solution {
    /**
     * Finds the minimum number of queries required to make all elements in 'nums' zero.
     * @param nums The input array of integers.
     * @param queries A 2D array where each query is [start_index, end_index, value_to_subtract].
     * @return The minimum number of queries needed, or -1 if it's not possible.
     */
    public int minZeroArray(int[] nums, int[][] queries) {
        int maxNum = 0;
        for (int num : nums) {
            if (num > maxNum) {
                maxNum = num;
            }
        }

        int left = 0;
        int right = queries.length;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(nums, queries, mid)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }

    private boolean check(int[] nums, int[][] queries, int k) {
        int[] buffer = new int[k];
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                continue;
            }
            
            int count = 0;
            int sum = 0;
            for (int j = 0; j < k; j++) {
                if (queries[j][0] <= i && queries[j][1] >= i) {
                    buffer[count++] = queries[j][2];
                    sum += queries[j][2];
                }
            }

            if (sum < nums[i]) {
                return false;
            }
            if (!canPartition(buffer, count, nums[i])) {
                return false;
            }
        }
        return true;
    }

    private boolean canPartition(int[] values, int count, int target) {
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        
        for (int i = 0; i < count; i++) {
            int val = values[i];
            for (int j = target; j >= val; j--) {
                if (dp[j - val]) {
                    dp[j] = true;
                }
            }
        }
        return dp[target];
    }
}