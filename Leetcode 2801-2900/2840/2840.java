// Leetcde 2840: Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
// Solved on 30th of March, 2026
class Solution {
    /**
     * Checks if two strings can be made equal by swapping characters at even indices 
     * with other even indices, and odd indices with other odd indices.
     * 
     * @param s1 The first input string.
     * @param s2 The second input string.
     * @return True if the strings can be made equal, false otherwise.
     */
    public boolean checkStrings(String s1, String s2) {
        int[] evenCounts = new int[26];
        int[] oddCounts = new int[26];
        int n = s1.length();
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                evenCounts[s1.charAt(i) - 'a']++;
                evenCounts[s2.charAt(i) - 'a']--;
            } else {
                oddCounts[s1.charAt(i) - 'a']++;
                oddCounts[s2.charAt(i) - 'a']--;
            }
        }
        
        for (int i = 0; i < 26; i++) {
            if (evenCounts[i] != 0 || oddCounts[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
}