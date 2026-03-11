// Leetcode 1009: Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/
// Solved on 11th of March, 2026
class Solution {
    /**
     * Returns the bitwise complement of a base-10 integer.
     * @param n The integer to complement.
     * @return The integer representing the bitwise complement.
     */
    public int bitwiseComplement(int n) {
        if (n == 0) {
            return 1;
        }
        int mask = n;
        mask |= mask >> 1;
        mask |= mask >> 2;
        mask |= mask >> 4;
        mask |= mask >> 8;
        mask |= mask >> 16;
        return n ^ mask;
    }
}