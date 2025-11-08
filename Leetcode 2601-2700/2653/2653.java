// Leetcode 2653: Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/
// Solved on 8th of November, 2025
class Solution {
    /**
     * Calculates the "beauty" of each subarray of length `k`.
     * The beauty is defined as the `x`-th smallest negative number in the subarray.
     * @param nums The input array of integers.
     * @param k The length of the subarrays.
     * @param x The rank of the negative number to find (e.g., 1st smallest, 2nd smallest).
     * @return An array containing the beauty of each subarray.
     */
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        int n = nums.length;
        int outLen = n - k + 1;
        int[] res = new int[outLen];
        int[] cnt = new int[51];
        int negatives = 0;
        for (int i = 0; i < k - 1; i++) {
            int v = nums[i];
            if (v < 0) {
                cnt[-v]++;
                negatives++;
            }
        }
        for (int i = k - 1; i < n; i++) {
            int add = nums[i];
            if (add < 0) {
                cnt[-add]++;
                negatives++;
            }
            if (negatives < x) {
                res[i - k + 1] = 0;
            } else {
                int need = x;
                int ans = 0;
                for (int idx = 50; idx >= 1; idx--) {
                    int c = cnt[idx];
                    if (c == 0) {
                        continue;
                    }
                    if (need > c) {
                        need -= c;
                    } else {
                        ans = -idx;
                        break;
                    }
                }
                res[i - k + 1] = ans;
            }
            int remove = nums[i - k + 1];
            if (remove < 0) {
                cnt[-remove]--;
                negatives--;
            }
        }
        return res;
    }
}