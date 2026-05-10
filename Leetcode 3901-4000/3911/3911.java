// Leetcode 3911: K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/
// Solved on 10th of May, 2026
class Solution {
    /**
     * Processes queries to find the k-th smallest remaining even integer in a subarray.
     *
     * @param nums    An array of integers.
     * @param queries A 2D array where each query is [l, r, k].
     * @return An array of integers containing the result for each query.
     */
    public int[] kthRemainingInteger(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] evenPrefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            evenPrefix[i + 1] = evenPrefix[i] + (nums[i] % 2 == 0 ? 1 : 0);
        }
        
        int q = queries.length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int k = queries[i][2];
            long low = k;
            long high = k + r - l + 1L;
            long res = k;
            
            while (low <= high) {
                long mid = low + (high - low) / 2;
                long target = mid * 2;
                int pos = findRightmost(nums, l, r, target);
                int count = evenPrefix[pos + 1] - evenPrefix[l];
                long remaining = mid - count;
                
                if (remaining >= k) {
                    res = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            ans[i] = (int) (res * 2);
        }
        return ans;
    }

    private int findRightmost(int[] nums, int left, int right, long target) {
        int pos = left - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target) {
                pos = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return pos;
    }
}