// Leetcode 693: Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/
// Solved on 18th of February, 2026
class Solution {
    /**
     * Checks if a positive integer has alternating bits (e.g., 101010).
     *
     * @param n The integer to check.
     * @return True if the binary representation of n has alternating bits, false otherwise.
     */
    public boolean hasAlternatingBits(int n) {
        int xorResult = n ^ (n >> 1);
        return (xorResult & (xorResult + 1)) == 0;
    }
}