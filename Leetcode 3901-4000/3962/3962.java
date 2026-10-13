// Leetcode 3962: Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/
// Solved on 13th of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Computes the maximum possible subarray sum after performing at most k swap operations
     * between any two elements in the array.
     *
     * @param nums the input array of integers
     * @param k the maximum number of allowed swap operations
     * @return the maximum possible subarray sum as a long integer
     */
    public long maxSum(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) {
            long maxSubarraySum = Long.MIN_VALUE;
            long currentSum = 0;
            for (int num : nums) {
                currentSum = Math.max(num, currentSum + num);
                maxSubarraySum = Math.max(maxSubarraySum, currentSum);
            }
            return maxSubarraySum;
        }

        long[] packed = new long[n];
        for (int i = 0; i < n; i++) {
            packed[i] = ((long) nums[i] << 32) | (i & 0xFFFFFFFFL);
        }
        Arrays.sort(packed);

        int[] sortedNums = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            sortedNums[i] = (int) (packed[i] >> 32);
            int originalIndex = (int) packed[i];
            rank[originalIndex] = i;
        }

        long[] topSum = new long[n + 1];
        for (int len = 1; len <= n; len++) {
            topSum[len] = topSum[len - 1] + sortedNums[n - len];
        }

        long maxResult = Long.MIN_VALUE;
        int maxDirectLen = Math.min(n, k);
        for (int len = 1; len <= maxDirectLen; len++) {
            maxResult = Math.max(maxResult, topSum[len]);
        }
        int minSuffixLen = Math.max(1, n - k);
        for (int len = minSuffixLen; len <= n; len++) {
            maxResult = Math.max(maxResult, topSum[len]);
        }

        if (2 * k + 2 > n) {
            return maxResult;
        }

        long initialOutSum = topSum[k];
        boolean[] inSub = new boolean[n];

        for (int left = 0; left <= n - k - 1; left++) {
            long baseSum = 0;
            int pOut = n - k;
            long sumOut = initialOutSum;

            for (int right = left; right < left + k; right++) {
                int pos = rank[right];
                inSub[pos] = true;
                baseSum += nums[right];
                if (pos >= pOut) {
                    pOut--;
                    while (inSub[pOut]) {
                        pOut--;
                    }
                    sumOut += sortedNums[pOut] - sortedNums[pos];
                }
            }

            int pIn = n - 1;
            long sumIn = baseSum;
            while (!inSub[pIn]) {
                pIn--;
            }

            int maxRight = Math.min(n - 1, left + n - k - 2);
            for (int right = left + k; right <= maxRight; right++) {
                int pos = rank[right];
                inSub[pos] = true;
                baseSum += nums[right];

                if (pos >= pOut) {
                    pOut--;
                    while (inSub[pOut]) {
                        pOut--;
                    }
                    sumOut += sortedNums[pOut] - sortedNums[pos];
                }

                if (pos < pIn) {
                    sumIn += sortedNums[pos] - sortedNums[pIn];
                    pIn--;
                    while (!inSub[pIn]) {
                        pIn--;
                    }
                }

                int currentLen = right - left + 1;
                long candidateSum = (pIn < pOut) ? (baseSum - sumIn + sumOut) : topSum[currentLen];
                maxResult = Math.max(maxResult, candidateSum);
            }

            for (int right = left; right <= maxRight; right++) {
                inSub[rank[right]] = false;
            }
        }

        return maxResult;
    }
}