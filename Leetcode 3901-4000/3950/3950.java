// Leetcode 3950: Exactly One Consecutive Set Bits Pair
// https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/
// Solved on 21st of June, 2026
class Solution {
    /**
     * Checks if a number has exactly one pair of consecutive set bits.
     *
     * @param n The number to check.
     * @return True if the number has exactly one pair of consecutive set bits,
     * false otherwise.
     */
    public boolean consecutiveSetBits(int n) {
        int pairMask = n & (n >> 1);
        return pairMask != 0 && (pairMask & (pairMask - 1)) == 0;
    }
}