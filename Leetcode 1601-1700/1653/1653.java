// Leetcode 1653: Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
// Solved on 7th of February, 2026
class Solution {
    /**
     * Calculates the minimum number of deletions to make a string balanced.
     * A string is balanced if there is no index i such that s[i] = 'b' and s[j] = 'a' where i < j.
     *
     * @param s The input string consisting of 'a's and 'b's.
     * @return The minimum number of deletions needed to make the string balanced.
     */
    public int minimumDeletions(String s) {
        int bCount = 0;
        int minDeletions = 0;
        int n = s.length();
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'b') {
                bCount++;
            } else {
                minDeletions = Math.min(minDeletions + 1, bCount);
            }
        }
        
        return minDeletions;
    }
}