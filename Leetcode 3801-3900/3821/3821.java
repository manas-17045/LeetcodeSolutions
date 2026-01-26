// Leetcode 3821: Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/
// Solved on 26th of January, 2026
class Solution {
    /**
     * Finds the nth smallest integer that has exactly k one bits in its binary representation.
     *
     * @param n The rank (1-indexed) of the integer to find.
     * @param k The number of set bits (one bits) required.
     * @return The nth smallest integer with k set bits.
     */
    public long nthSmallest(long n, int k) {
        long[][] combinations = new long[60][60];
        for (int i = 0; i < 60; i++) {
            combinations[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j];
            }
        }

        long result = 0;
        while (k > 0) {
            int len = k;
            while (combinations[len][k] < n) {
                len++;
            }
            result |= (1L << (len - 1));
            n -= combinations[len - 1][k];
            k--;
        }
        
        return result;
    }
}