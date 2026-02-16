// Leetcode 190: Reverse Bits
// https://leetcode.com/problems/reverse-bits/
// Solved on 16th of February, 2026
class Solution{
    /**
     * Reverses the bits of a given 32-bit unsigned integer.
     *
     * @param n the input integer
     * @return the integer formed by reversing the bits of n
     */
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>>= 1;
        }
        return result;
    }
}