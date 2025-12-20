// Leetcode 3681: Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/
// Solved on 20th of December, 2025
class Solution {
    /**
     * Finds the maximum XOR sum of any subsequence of the given array.
     * This is achieved by constructing a Gaussian basis (or XOR basis) for the numbers.
     * @param nums The input array of integers.
     * @return The maximum possible XOR sum of a subsequence.
     */
    public int maxXorSubsequences(int[] nums) {
        int[] basis = new int[32];
        for (int num : nums) {
            for (int i = 30; i >= 0; i--) {
                if ((num & (1 << i)) != 0) {
                    if (basis[i] == 0) {
                        basis[i] = num;
                        break;
                    }
                    num ^= basis[i];
                }
            }
        }

        int max = 0;
        for (int i = 30; i >= 0; i--) {
            if ((max ^ basis[i]) > max) {
                max ^= basis[i];
            }
        }
        return max;
    }
}