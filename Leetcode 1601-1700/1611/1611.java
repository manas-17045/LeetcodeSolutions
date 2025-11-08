// Leetcode 1611: Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
// Solved on 8th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of one-bit operations required to make the integer n zero.
     * @param n The input integer.
     * @return The minimum number of one-bit operations.
     */
    public int minimumOneBitOperations(int n) {
        if (n == 0) {
            return 0;
        }
        int maxBit = 31 - Integer.numberOfLeadingZeros(n);
        int res = 0;
        for (int i = 0; i < maxBit; i++) {
            if (((n >> i) & 1) == 1) {
                int mask = (1 << (i + 1)) - 1;
                res = mask - res;
            }
        }
        return res;
    }
}