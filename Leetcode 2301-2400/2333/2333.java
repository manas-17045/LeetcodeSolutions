// Leetcode 2333: Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/
// Solved on 10th of October, 2026
class Solution {
    /**
     * Calculates the minimum sum of squared differences between two arrays
     * after modifying elements in both arrays within their given operation limits.
     *
     * @param nums1 the first integer array
     * @param nums2 the second integer array
     * @param k1 the maximum number of modifications allowed on nums1
     * @param k2 the maximum number of modifications allowed on nums2
     * @return the minimum possible sum of squared differences
     */
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int length = nums1.length;
        int maxDiff = 0;
        long totalDiff = 0;
        long totalK = (long) k1 + k2;
        int[] frequency = new int[100001];

        for (int i = 0; i < length; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            frequency[diff]++;
            totalDiff += diff;
            if (diff > maxDiff) {
                maxDiff = diff;
            }
        }

        if (totalK >= totalDiff) {
            return 0L;
        }

        for (int diff = maxDiff; diff > 0 && totalK > 0; diff--) {
            if (frequency[diff] == 0) {
                continue;
            }

            if (totalK >= frequency[diff]) {
                frequency[diff - 1] += frequency[diff];
                totalK -= frequency[diff];
                frequency[diff] = 0;
            } else {
                frequency[diff - 1] += (int) totalK;
                frequency[diff] -= (int) totalK;
                totalK = 0;
            }
        }

        long minSum = 0;
        for (int diff = 1; diff <= maxDiff; diff++) {
            if (frequency[diff] > 0) {
                minSum += (long) frequency[diff] * diff * diff;
            }
        }

        return minSum;
    }
}