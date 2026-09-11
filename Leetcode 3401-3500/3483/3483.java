// Leetcode 3483: Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/
// Solved on 11th of September, 2026
class Solution {
    /**
     * Calculates the number of distinct three-digit even numbers that can be
     * formed using the given digits without leading zeros.
     *
     * @param digits an array of integers representing available digits
     * @return the count of unique three-digit even numbers that can be created
     */
    public int totalNumbers(int[] digits) {
        int[] digitCounts = new int[10];
        for (int digit : digits) {
            digitCounts[digit]++;
        }

        int count = 0;
        for (int num = 100; num < 1000; num += 2) {
            int hundreds = num / 100;
            int tens = (num / 10) % 10;
            int units = num % 10;

            digitCounts[hundreds]--;
            digitCounts[tens]--;
            digitCounts[units]--;

            if (digitCounts[hundreds] >= 0 && digitCounts[tens] >= 0 && digitCounts[units] >= 0) {
                count++;
            }

            digitCounts[hundreds]++;
            digitCounts[tens]++;
            digitCounts[units]++;
        }

        return count;
    }
}