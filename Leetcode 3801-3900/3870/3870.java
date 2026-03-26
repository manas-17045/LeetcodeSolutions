// Leetcode 3870: Count Commas in Range
// https://leetcode.com/problems/count-commas-in-range/
// Solved on 26th of March, 2026
class Solution {
    /**
     * Counts the total number of commas used when writing all integers from 1 to n.
     *
     * @param n The upper bound of the range (inclusive).
     * @return The total count of commas in the range [1, n].
     */
    public int countCommas(int n) {
        int result = 0;
        if (n >= 1000) {
            result += n - 999;
        }
        if (n >= 1000000) {
            result += n - 999999;
        }
        if (n >= 1000000000) {
            result += n - 999999999;
        }
        return result;
    }
}