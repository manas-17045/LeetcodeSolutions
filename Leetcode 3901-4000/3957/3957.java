// Leetcode 3957: Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/
// Solved on 27th of June, 2026
class Solution {
    /**
     * This problem asks for the maximum sum of m non-overlapping subarrays, each of length between l and r (inclusive).
     *
     * @param nums array of integers
     * @param m number of non-overlapping subarrays
     * @param l minimum length of each subarray
     * @param r maximum length of each subarray
     * @return maximum sum of m non-overlapping subarrays of length between l and r (inclusive)
     */
    public long maximumSum(int[] nums, int m, int l, int r) {
        int n = nums.length;
        long[] pref = new long[n + 1];
        
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        
        long maxSingle = Long.MIN_VALUE;
        int head = 0;
        int tail = 0;
        int[] minQ = new int[n + 1];
        
        for (int i = l; i <= n; i++) {
            int newJ = i - l;
            while (head < tail && pref[minQ[tail - 1]] >= pref[newJ]) {
                tail--;
            }
            minQ[tail++] = newJ;
            
            while (head < tail && minQ[head] < i - r) {
                head++;
            }
            
            long curSingle = pref[i] - pref[minQ[head]];
            if (curSingle > maxSingle) {
                maxSingle = curSingle;
            }
        }
        
        if (maxSingle <= 0) {
            return maxSingle;
        }
        
        long low = 0;
        long high = 20000000000L;
        long ans = 0;
        
        long[] dp = new long[n + 1];
        long[] cnt = new long[n + 1];
        int[] q = new int[n + 1];
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            
            head = 0;
            tail = 0;
            
            for (int i = 1; i <= n; i++) {
                dp[i] = dp[i - 1];
                cnt[i] = cnt[i - 1];
                
                if (i >= l) {
                    int newJ = i - l;
                    long valNew = dp[newJ] - pref[newJ];
                    long cNew = cnt[newJ];
                    
                    while (head < tail) {
                        int backJ = q[tail - 1];
                        long valBack = dp[backJ] - pref[backJ];
                        long cBack = cnt[backJ];
                        
                        if (valNew > valBack || (valNew == valBack && cNew >= cBack)) {
                            tail--;
                        } else {
                            break;
                        }
                    }
                    q[tail++] = newJ;
                }
                
                while (head < tail && q[head] < i - r) {
                    head++;
                }
                
                if (head < tail) {
                    int bestJ = q[head];
                    long candVal = dp[bestJ] - pref[bestJ] + pref[i] - mid;
                    long candCnt = cnt[bestJ] + 1;
                    
                    if (candVal > dp[i] || (candVal == dp[i] && candCnt > cnt[i])) {
                        dp[i] = candVal;
                        cnt[i] = candCnt;
                    }
                }
            }
            
            if (mid == 0 && cnt[n] <= m) {
                return dp[n];
            }
            
            if (cnt[n] >= m) {
                ans = dp[n] + m * mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return ans;
    }
}