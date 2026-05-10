// Leetcode 3915: Maximum Sum of Alternating Subsequence With Distance at Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/
// Solved on 10th of May, 2026
class Solution {
    /**
     * Calculates the maximum sum of an alternating subsequence where each adjacent 
     * element in the subsequence is at least distance k apart in the original array.
     *
     * @param nums The input array of integers.
     * @param k    The minimum distance required between indices of chosen elements.
     * @return The maximum sum of a valid alternating subsequence.
     */
    public long maxAlternatingSum(int[] nums, int k) {
        int n = nums.length;
        int maxVal = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > maxVal) {
                maxVal = nums[i];
            }
        }
        long[] valleyTree = new long[maxVal + 1];
        long[] peakTree = new long[maxVal + 1];
        long[] dp0 = new long[n];
        long[] dp1 = new long[n];
        long result = 0;
        for (int i = 0; i < n; i++) {
            if (i - k >= 0) {
                int prevIdx = i - k;
                int prevVal = nums[prevIdx];
                long peakVal = dp0[prevIdx];
                long valleyVal = dp1[prevIdx];
                for (int j = prevVal; j <= maxVal; j += j & -j) {
                    if (valleyVal > valleyTree[j]) {
                        valleyTree[j] = valleyVal;
                    }
                }
                int revIdx = maxVal - prevVal + 1;
                for (int j = revIdx; j <= maxVal; j += j & -j) {
                    if (peakVal > peakTree[j]) {
                        peakTree[j] = peakVal;
                    }
                }
            }
            int currentVal = nums[i];
            long maxValleyPrefix = 0;
            for (int j = currentVal - 1; j > 0; j -= j & -j) {
                if (valleyTree[j] > maxValleyPrefix) {
                    maxValleyPrefix = valleyTree[j];
                }
            }
            dp0[i] = maxValleyPrefix + currentVal;
            if (currentVal > dp0[i]) {
                dp0[i] = currentVal;
            }
            long maxPeakSuffix = 0;
            int revCurrentIdx = maxVal - currentVal;
            for (int j = revCurrentIdx; j > 0; j -= j & -j) {
                if (peakTree[j] > maxPeakSuffix) {
                    maxPeakSuffix = peakTree[j];
                }
            }
            dp1[i] = maxPeakSuffix + currentVal;
            if (currentVal > dp1[i]) {
                dp1[i] = currentVal;
            }
            if (dp0[i] > result) {
                result = dp0[i];
            }
            if (dp1[i] > result) {
                result = dp1[i];
            }
        }
        return result;
    }
}