// Leetcode 3783: Mirror Distance of an Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/
// Solved on 18th of April, 2026
class Solution {
    /**
     * Calculates the absolute difference between an integer and its reverse.
     *
     * @param n The integer to process.
     * @return The absolute difference between n and its mirror (reversed) value.
     */
    public int mirrorDistance(int n) {
        int originalValue = n;
        int reversedValue = 0;

        while (n > 0) {
            reversedValue = reversedValue * 10 + n % 10;
            n /= 10;
        }

        return Math.abs(originalValue - reversedValue);
    }
}