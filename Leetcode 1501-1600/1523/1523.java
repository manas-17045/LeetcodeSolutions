// Leetcode 1523: Count Odd Numbers in an Interval Range
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
// Solved on 7th of December, 2025
class Solution {
    /**
     * Counts the number of odd integers within a given interval [low, high].
     *
     * @param low The lower bound of the interval (inclusive).
     * @param high The upper bound of the interval (inclusive).
     * @return The count of odd numbers in the interval.
     */
    public int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}