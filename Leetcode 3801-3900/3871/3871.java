// Leetcode 3871: Count Commas in Range II
// https://leetcode.com/problems/count-commas-in-range-ii/
// Solved on 27th of March, 2026
class Solution {
    /**
     * Calculates the total number of commas used when writing all integers from 1 to n.
     * @param n The upper bound of the range (inclusive).
     * @return The total count of commas in the range [1, n].
     */
    public long countCommas(long n) {
        long totalCommas = 0;
        long base = 1000;

        while (n >= base) {
            totalCommas += n - base + 1;
            base *= 1000;
        }

        return totalCommas;
    }
}