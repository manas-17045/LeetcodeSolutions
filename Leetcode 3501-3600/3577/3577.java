// Leetcode 3577: Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
// Solved on 10th of December, 2025
class Solution {
    /**
     * Given an array `complexity` representing the complexity of `n` computers,
     * return the number of valid permutations to unlock them.
     * @param complexity An array of integers representing the complexity of each computer.
     * @return The number of valid permutations modulo 10^9 + 7.
     */
    public int countPermutations(int[] complexity) {
        int n = complexity.length;
        long modulo = 1000000007;
        int rootComplexity = complexity[0];

        for (int i = 1; i < n; i++) {
            if (complexity[i] <= rootComplexity) {
                return 0;
            }
        }

        long validPermutations = 1;
        for (int i = 1; i < n; i++) {
            validPermutations = (validPermutations * i) % modulo;
        }

        return (int) validPermutations;
    }
}