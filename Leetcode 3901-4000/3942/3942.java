// Leetcode 3942: Minimum Operations to Sort a Permutation
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
// Solved on 7th of June, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to sort a permutation.
     * @param nums An array representing a permutation of integers.
     * @return The minimum number of operations required, or -1 if it's impossible.
     */
    public int minOperations(int[] nums) {
        int n = nums.length;
        int zeroIdx = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zeroIdx = i;
                break;
            }
        }

        boolean isIncreasing = true;
        for (int i = 1; i < n; i++) {
            int prev = (zeroIdx + i - 1) % n;
            int curr = (zeroIdx + i) % n;
            if (nums[prev] > nums[curr]) {
                isIncreasing = false;
                break;
            }
        }

        boolean isDecreasing = true;
        for (int i = 1; i < n; i++) {
            int prev = (zeroIdx - (i - 1) + n) % n;
            int curr = (zeroIdx - i + n) % n;
            if (nums[prev] > nums[curr]) {
                isDecreasing = false;
                break;
            }
        }

        int ans = Integer.MAX_VALUE;
        if (isIncreasing) {
            ans = Math.min(ans, zeroIdx);
            ans = Math.min(ans, n - zeroIdx + 2);
        }
        if (isDecreasing) {
            ans = Math.min(ans, zeroIdx + 2);
            ans = Math.min(ans, n - zeroIdx);
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}