// Leetcode 796: Rotate String
// https://leetcode.com/problems/rotate-string/
// Solved on 3rd of May, 2026
class Solution {
    /**
     * Checks if the string s can become the string goal after some number of shifts.
     * 
     * @param s The source string.
     * @param goal The target string to match after rotation.
     * @return true if s can become goal, false otherwise.
     */
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        
        String doubledString = s + s;
        return doubledString.contains(goal);
    }
}