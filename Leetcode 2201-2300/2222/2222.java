// Leetcode 2222: Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/
// Solved on 28th of November, 2025
class Solution {
    /**
     * Calculates the number of ways to select three buildings such that they are not all of the same type.
     * The selection must be in the order of indices (i < j < k).
     *
     * @param s A binary string representing the types of buildings ('0' for one type, '1' for another).
     * @return The total number of valid ways to select three buildings.
     */
    public long numberOfWays(String s) {
        long zeroCount = 0;
        long oneCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                zeroCount++;
            } else {
                oneCount++;
            }
        }

        long ans = 0;
        long currentZero = 0;
        long currentOne = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                ans += currentOne * (oneCount - currentOne);
                currentZero++;
            } else {
                ans += currentZero * (zeroCount - currentZero);
                currentOne++;
            }
        }

        return ans;
    }
}