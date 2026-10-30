// Leetcode 4063: Longest Subarray Divisible by K with At Most One Negation I
// https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-i/
// Solved on 30th of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the length of the longest subarray whose sum is divisible by k,
     * either directly or after negating at most one element within the subarray.
     *
     * @param nums the input array of integers
     * @param k the divisor
     * @return the maximum length of a valid subarray, or 0 if none exists
     */
    public int longestSubarray(int[] nms, int k) {
        int[] earliestZero = new int[k];
        int[] earliestOne = new int[k];
        Arrays.fill(earliestZero, -1);
        Arrays.fill(earliestOne, -1);

        int[] prefixList = new int[nums.length + 1];
        int prefixCount = 0;

        earliestZero[0] = 0;
        prefixList[prefixCount++] = 0;

        int currentRemainder = 0;
        int maxLength = 0;

        for (int t = 0; t < nums.length; t++) {
            long doubled = ((long) 2 * nums[t]) % k;
            if (doubled < 0) {
                doubled += k;
            }
            int doubledRemainder = (int) doubled;

            for (int i = 0; i < prefixCount; i++) {
                int p = prefixList[i];
                int targetRemainder = p + doubledRemainder;
                if (targetRemainder >= k) {
                    targetRemainder -= k;
                }
                if (earliestOne[targetRemainder] == -1 || earliestZero[p] < earliestOne[targetRemainder]) {
                    earliestOne[targetRemainder] = earliestZero[p];
                }
            }

            currentRemainder = (int) (((currentRemainder + nums[t]) % k + k) % k);

            if (earliestZero[currentRemainder] != -1) {
                maxLength = Math.max(maxLength, (t + 1) - earliestZero[currentRemainder]);
            }

            if (earliestOne[currentRemainder] != -1) {
                maxLength = Math.max(maxLength, (t + 1) - earliestOne[currentRemainder]);
            }

            if (earliestZero[currentRemainder] == -1) {
                earliestZero[currentRemainder] = t + 1;
                prefixList[prefixCount++] = currentRemainder;
            }
        }

        return maxLength;
    }
}