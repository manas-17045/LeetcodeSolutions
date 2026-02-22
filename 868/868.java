// Leetcode 868: Binary Gap
// https://leetcode.com/problems/binary-gap/
// Solved on 22nd of February, 2026
class Solution {
    /**
     * Calculates the longest distance between two adjacent 1's in the binary representation of n.
     *
     * @param n The input integer.
     * @return The maximum distance between two adjacent 1's, or 0 if no such pair exists.
     */
    public int binaryGap(int n) {
        while ((n & 1) == 0) {
            n >>= 1;
        }
        int maxGap = 0;
        int currentGap = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if (currentGap > maxGap) {
                    maxGap = currentGap;
                }
                currentGap = 1;
            } else {
                currentGap++;
            }
            n >>= 1;
        }
        return maxGap;
    }
}