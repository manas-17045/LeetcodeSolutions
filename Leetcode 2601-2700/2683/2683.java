// Leetcode 2683: Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/
// Solved on 12th of November, 2025
class Solution {
    /**
     * Checks if a valid original binary array `original` exists such that `derived[i] = original[i] ^ original[(i + 1) % n]`.
     * This is possible if and only if the XOR sum of all elements in `derived` is 0.
     *
     * @param derived The derived array, where `derived[i]` is the XOR of `original[i]` and `original[(i + 1) % n]`.
     * @return `true` if a valid original array exists, `false` otherwise.
     */
    public boolean doesValidArrayExist(int[] derived) {
        int xorSum = 0;
        for (int v : derived) {
            xorSum ^= v;
        }

        return xorSum == 0;
    }
}