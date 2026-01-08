// Leetcode 3790: Smallest All-Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/
// Solved on 8th of January, 2026
class Solution {
    /**
     * Finds the length of the smallest "all-ones" number (e.g., 1, 11, 111) that is a multiple of k.
     *
     * @param k The integer to check for its all-ones multiple.
     * @return The length of the smallest all-ones multiple, or -1 if no such multiple exists.
     */
    public int minAllOneMultiple(int k) {
        if (k % 2 == 0 || k % 5 == 0) {
            return -1;
        }

        int remainder = 0;

        for (int length = 1; length <= k; length++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) {
                return length;
            }
        }

        return -1;
    }
}