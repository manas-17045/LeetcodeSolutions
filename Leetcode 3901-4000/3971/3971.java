// Leetcode 3971: Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/
// Solved on 13th of July, 2026
class Solution {
    /**
     * Calculates the maximum total value that can be obtained by selecting m items
     * from n items, each with a specific value and decay rate
     * 
     * @param value values of the items
     * @param decay decay rates of the items
     * @param m number of items to take
     * @return maximum total value
     */
    public int maxTotalValue(int[] value, int[] decay, int m) {
        long left = 1;
        long right = 0;
        for (int v : value) {
            if (v > right) {
                right = v;
            }
        }
        
        long threshold = 0;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            long count = 0;
            
            for (int i = 0; i < value.length; i++) {
                if (value[i] >= mid) {
                    count += (value[i] - mid) / decay[i] + 1;
                }
            }
            
            if (count >= m) {
                threshold = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        long totalSum = 0;
        long taken = 0;
        long target = threshold + 1;
        long mod = 1000000007;
        
        for (int i = 0; i < value.length; i++) {
            if (value[i] >= target) {
                long terms = (value[i] - target) / decay[i] + 1;
                taken += terms;
                
                long first = value[i];
                long last = value[i] - (terms - 1) * (long) decay[i];
                long apSum = terms * (first + last) / 2;
                
                totalSum = (totalSum + apSum % mod) % mod;
            }
        }
        
        if (threshold > 0) {
            long remaining = m - taken;
            long added = (remaining * threshold) % mod;
            totalSum = (totalSum + added) % mod;
        }
        
        return (int) totalSum;
    }
}