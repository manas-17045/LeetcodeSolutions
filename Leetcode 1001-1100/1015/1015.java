// Leetcode 1015: Smallest Integer Divisible by K
// https://leetcode.com/problems/smallest-integer-divisible-by-k/
// Solved on 25th of November, 2025
class Solution {
    /**
     * Finds the length of the smallest positive integer N consisting only of digit 1s that is divisible by K.
     *
     * @param k The integer divisor.
     * @return The length of the smallest such integer N, or -1 if no such integer exists.
     */
    public smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }
        int remainder = 0;
        for (int length = 1; length <= k; length++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) {
                return length;
            }
        }
        return -1;
    }
}