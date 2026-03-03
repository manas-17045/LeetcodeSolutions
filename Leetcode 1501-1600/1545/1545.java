// Leetcode 1545: Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
// Solved on 3rd of March, 2026
class Solution {
    /**
     * Finds the kth bit in the nth binary string Sn.
     *
     * @param n The index of the binary string sequence.
     * @param k The 1-indexed position of the bit to find.
     * @return The kth bit as a character ('0' or '1').
     */
    public char findKthBit(int n, int k) {
        int invertCount = 0;
        int currentLength = (1 << n) - 1;
        while (k > 1) {
            if (k == currentLength / 2 + 1) {
                return invertCount % 2 == 0 ? '1' : '0';
            }
            if (k > currentLength / 2) {
                k = currentLength - k + 1;
                invertCount++;
            }
            currentLength /= 2;
        }
        return invertCount % 2 == 0 ? '0' : '1';
    }
}