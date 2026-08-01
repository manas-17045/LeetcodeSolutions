// Leetcode 3982: Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/
// Solved on 1st of August, 2026
class Solution {
    /**
     * Calculates the sum of all integers in the input array that have the maximum
     * digit range among all integers.
     *
     * The digit range of an integer is defined as the difference between its largest
     * and smallest digits.
     *
     * @param nums An array of integers.
     * @return The sum of all integers in the array that have the maximum digit
     *         range.
     */
    public long maxDigitRange(int[] nums) {
        int maxRange = -1;
        int totalSum = 0;

        for (int num : nums) {
            int tempNum = num;
            int minDigit = 9;
            int maxDigit = 0;

            while (tempNum > 0) {
                int currentDigit = tempNum % 10;
                if (currentDigit < minDigit) {
                    minDigit = currentDigit;
                }
                if (currentDigit > maxDigit) {
                    maxDigit = currentDigit;
                }
                tempNum /= 10;
            }

            int currentRange = maxDigit - minDigit;

            if (currentRange > maxRange) {
                maxRange = currentRange;
                totalSum = num;
            } else if (currentRange == maxRange) {
                totalSum += num;
            }
        }

        return totalSum;
    }
}