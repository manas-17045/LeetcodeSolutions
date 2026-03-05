// Leetcode 1758: Minimum Changes To make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
// Solved on 5th of March, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to make a binary string alternating.
     * 
     * @param s The input binary string consisting of '0's and '1's.
     * @return The minimum number of character flips needed to make the string alternating.
     */
    public int minOperations(String s) {
        int count = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) - '0' != i % 2){
                count++;
            }
        }
        return Math.min(count, n - count);
    }
}