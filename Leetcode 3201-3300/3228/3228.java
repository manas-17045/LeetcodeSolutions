// Leetcode 3228: Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
// Solved on 13th of November, 2025
class Solution {
    /**
     * Calculates the maximum number of operations to move all '1's to the end of the binary string.
     * An operation consists of moving a '1' to the end of the string.
     *
     * @param s The input binary string.
     * @return The maximum number of operations.
     */
    public int maxOperations(String s) {
        int ans = 0;
        int ones = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            if (c == '1') {
                ones++;
            } else if (i == n - 1 || s.charAt(i + 1) == '1') {
                ans += ones;
            }
        }
        return ans;
    }
}