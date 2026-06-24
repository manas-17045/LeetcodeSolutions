// Leetcode 3954: Sum of Compatible Numbers in Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/
// Solved on 24th of June, 2026
class Solution {
    /**
     * Calculates the sum of compatible numbers in the range.
     *
     * @param n The base number.
     * @param k The range parameter.
     * @return The sum of compatible numbers in the range [max(1, n - k), n + k] such that (n & num) == 0.
     */
    public int sumOfGoodIntegers(int n, int k) {
        int totalSum = 0;
        int start = Math.max(1, n - k);
        int end = n + k;

        for (int x = start; x <= end; x++) {
            if ((n & x) == 0) {
                totalSum += x;
            }
        }

        return totalSum;
    }
}