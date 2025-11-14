// Leetcode 1529: Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/
// Solved on 14th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of suffix flips required to transform an initial string of all '0's to the target string.
     * @param target The target string consisting of '0's and '1's.
     * @return The minimum number of flips.
     */
    public int minFlips(String target) {
        int flips = 0;
        char prev = '0';
        for (int i = 0; i < target.length(); i++) {
            char c = target.charAt(i);
            if (c != prev) {
                flips++;
                prev = c;
            }
        }
        return flips;
    }
}