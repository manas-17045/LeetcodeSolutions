// Leetcode 4032: Longest Subarray With at Most K Distinct Prime Factors
// https://leetcode.com/problems/longest-subarrays-with-at-most-k-distinct-prime-factors/
// Solved on 24th of September, 2026
class Solution {
    /**
     * Finds the length of the longest subarray whose prime factor set contains
     * at most k distinct prime factors.
     *
     * @param nums the array of positive integers
     * @param k the maximum allowed number of distinct prime factors
     * @return the maximum length of such a subarray, or 0 if none exists
     */
    public int longestSubarray(int[] nums, int k) {
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }

        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            spf[i] = i;
        }
        for (int i = 2; i * i <= maxVal; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxVal; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }

        int[] count = new int[maxVal + 1];
        int distinctPrimes = 0;
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < nums.length; right++) {
            int temp = nums[right];
            while (temp > 1) {
                int prime = spf[temp];
                if (count[prime] == 0) {
                    distinctPrimes++;
                }
                count[prime]++;
                while (temp > 1 && spf[temp] == prime) {
                    temp /= prime;
                }
            }

            while (distinctPrimes > k) {
                int leftTemp = nums[left];
                while (leftTemp > 1) {
                    int prime = spf[leftTemp];
                    count[prime]--;
                    if (count[prime] == 0) {
                        distinctPrimes--;
                    }
                    while (leftTemp > 1 && spf[leftTemp] == prime) {
                        leftTemp /= prime;
                    }
                }
                left++;
            }

            if (left <= right) {
                maxLength = Math.max(maxLength, right - left + 1);
            }
        }

        return maxLength;
    }
}