// Leetcode 3654: Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/
// Solved on 29th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum possible sum of remaining elements after performing a series of deletions.
     * A deletion involves removing a subarray such that its sum is divisible by `k`.
     * @param nums The input array of integers.
     * @param k The divisor for the subarray sums.
     * @return The minimum sum of elements after deletions.
     */
    public long minArraySum(int[] nums, int k) {
        long[] maxVal = new long[k];
        Arrays.fill(maxVal, Long.MIN_VALUE);
        maxVal[0] = 0;

        long currentDp = 0;
        long prefixSum = 0;

        for (int num : nums) {
            prefixSum += num;
            int mod = (int) (prefixSum % k);

            if (maxVal[mod] != Long.MIN_VALUE) {
                currentDp = Math.max(currentDp, maxVal[mod] + prefixSum);
            }

            maxVal[mod] = Math.max(maxVal[mod], currentDp - prefixSum);
        }

        return prefixSum - currentDp;
    }
}