// Leetcode 2839: Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
// Solved on 29th of March, 2026
class Solution {
    /**
     * Checks if two strings of length 4 can be made equal by swapping characters at indices i and j
     * such that j - i = 2.
     * @param s1 The first string of length 4.
     * @param s2 The second string of length 4.
     * @return true if s1 can be made equal to s2, false otherwise.
     */
    public boolean canBeEqual(String s1, String s2) {
        boolean checkEven = (s1.charAt(0) == s2.charAt(0) && s1.charAt(2) == s2.charAt(2)) || 
                            (s1.charAt(0) == s2.charAt(2) && s1.charAt(2) == s2.charAt(0));
        boolean checkOdd = (s1.charAt(1) == s2.charAt(1) && s1.charAt(3) == s2.charAt(3)) || 
                           (s1.charAt(1) == s2.charAt(3) && s1.charAt(3) == s2.charAt(1));
        return checkEven && checkOdd;
    }
}