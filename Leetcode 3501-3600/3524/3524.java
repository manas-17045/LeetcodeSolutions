// Leetcode 3524: Find X Value of Array I
// https://leetcode.com/problems/find-x-value-of-array-i/
// Solved on 21st of Septemeber, 2026
class Solution {
    /**
     * Calculates the number of non-empty subarrays whose product leaves a remainder
     * of x when divided by k, for each remainder from 0 to k - 1.
     *
     * @param nums the array of positive integers
     * @param k the positive integer divisor
     * @return an array where the value at index x is the count of subarrays with product modulo k equal to x
     */
    public long[] resultArray(int[] nums, int k) {
        long[] result = new long[k];
        long[] currentCounts = new long[k];

        for (int num : nums) {
            long[] nextCounts = new long[k];
            int remainder = num % k;

            nextCounts[remainder]++;

            for (int r = 0; r < k; r++) {
                if (currentCounts[r] > 0) {
                    int nextRemainder = (r * remainder) % k;
                    nextCounts[nextRemainder] += currentCounts[r];
                }
            }

            for (int r = 0; r < k; r++) {
                result[r] += nextCounts[r];
            }

            currentCounts = nextCounts;
        }

        return result;
    }
}