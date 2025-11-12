// Leetcode 1806: Minimum Number of Operations to reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
// Solved on 12th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to reinitialize a permutation of size `n`.
     * A permutation `perm` of size `n` is reinitialized when `perm[i] == i` for all `i`.
     * @param n The size of the permutation.
     * @return The minimum number of operations required.
     */
    public int reinitializePermutation(int n) {
        int count = 0;
        int pos = 1;
        do {
            pos = (pos % 2 == 0) ? pos / 2 : n / 2 + (pos - 1) / 2;
            count++;
        } while (pos != 1);
        return count;
    }
}