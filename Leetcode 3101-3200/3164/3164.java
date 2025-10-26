// Leetcode 3164: Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/
// Solved on 26th of October, 2025
import java.util.Map;
import java.util.HashMap;

class Solution {
    /**
     * Finds the number of good pairs (i, j) such that nums1[i] is divisible by nums2[j] * k.
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @param k The integer multiplier.
     * @return The total number of good pairs.
     */
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        long totalPairs = 0;

        if (nums1.length == 0 || nums2.length == 0) {
            return 0;
        }

        int maxNum1 = 0;
        for (int num : nums1) {
            if (num > maxNum1) {
                maxNum1 = num;
            }
        }

        int[] freq1 = new int[maxNum1 + 1];
        for (int num : nums1) {
            freq1[num]++;
        }

        Map<Integer, Integer> freq2 = new HashMap<>();
        for (int num : nums2) {
            freq2.put(num, freq2.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : freq2.entrySet()) {
            int val2 = entry.getKey();
            int count2 = entry.getValue();

            long divisor = (long) val2 * k;

            if (divisor > maxNum1) {
                continue;
            }

            for (long multiple = divisor; multiple <= maxNum1; multiple += divisor) {
                totalPairs += (long) freq1[(int) multiple] * count2;
            }
        }

        return totalPairs;
    }
}