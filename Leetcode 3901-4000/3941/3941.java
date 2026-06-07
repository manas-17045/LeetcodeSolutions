// Leetcode 3941: Password Strength
// https://leetcode.com/problems/password-strength/
// Solved on 7th of June, 2026
class Solution {
    /**
     * Calculates the strength of a password based on unique character types.
     * @param password The input string to evaluate.
     * @return The total calculated strength score.
     */
    public int passwordStrength(String password) {
        boolean[] seen = new boolean[128];
        int totalStrength = 0;
        for (int i = 0; i < password.length(); i++) {
            char ch = password.charAt(i);
            if (!seen[ch]) {
                seen[ch] = true;
                if (ch >= 'a' && ch <= 'z') {
                    totalStrength += 1;
                } else if (ch >= 'A' && ch <= 'Z') {
                    totalStrength += 2;
                } else if (ch >= '0' && ch <= '9') {
                    totalStrength += 3;
                } else if (ch == '!' || ch == '@' || ch == '#' || ch == '$') {
                    totalStrength += 5;
                }
            }
        }
        return totalStrength;
    }
}