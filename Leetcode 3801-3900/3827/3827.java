// Leetcode 3827: Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/
// Solved on 7th of February, 2026
class Solution {
    /**
     * Counts the number of monobit integers (integers whose binary representation consists only of 1s)
     * that are less than or equal to a given integer n.
     *
     * @param n The upper limit integer.
     * @return The total count of monobit integers up to n.
     */
    public int countMonobit(int n) {
        int count = 1;
        int val = 1;
        while (val <= n) {
            count++;
            val = (val << 1) | 1;
        }
        return count;
    }
}