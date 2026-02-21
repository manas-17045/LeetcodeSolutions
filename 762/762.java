// Leetcode 762: Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
// Solved on 21st of February, 2026
class Solution {
    /**
     * Counts the number of integers in the range [left, right] that have a 
     * prime number of set bits in their binary representation.
     * 
     * @param left The starting integer of the range (inclusive).
     * @param right The ending integer of the range (inclusive).
     * @return The total count of numbers with a prime number of set bits.
     */
    public int countPrimeSetBits(int left, int right) {
        int count = 0;
        for (int i = left; i <= right; i++) {
            int bits = Integer.bitCount();
            if (bits == 2 || bits == 5 || bits == 3 || bits == 7 || bits == 11 || bits == 13 || bits == 17 || bits == 19) {
                count++;
            }
        }
        return count;
    }
}