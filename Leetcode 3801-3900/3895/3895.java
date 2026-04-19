// Leetcode 3895: Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/
// Solved on 19th of April, 2026
class Solution {
    /**
     * Counts the total number of times a specific digit appears across all integers in an array.
     *
     * @param nums An array of integers to search through.
     * @param digit The specific digit (0-9) to count occurrences of.
     * @return The total count of the specified digit's appearances in the array.
     */
    public int countDigitOccurrences(int[] nums, int digit) {
        int totalCount = 0;
        for (int currentNum : nums) {
            int tempNum = currentNum;
            while (tempNum > 0) {
                if (tempNum % 10 == digit) {
                    totalCount++;
                }
                tempNum /= 10;
            }
        }
        return totalCount;
    }
}