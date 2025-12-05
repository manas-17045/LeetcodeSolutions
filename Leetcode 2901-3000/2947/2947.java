// Leetcode 2947: Count Beautiful Substrings I
// https://leetcode.com/problems/count-beautiful-substrings-i/
// Solved on 5th of December, 2025
class Solution {
    /**
     * Given a string s and an integer k, return the number of beautiful substrings.
     * A substring is beautiful if the number of vowels and consonants are equal, and (vowels * consonants) % k == 0.
     * @param s The input string.
     * @param k The integer k.
     * @return The number of beautiful substrings.
     */
    public int beautifulSubstrings(String s, int k) {
        int n = s.length();
        int d = 1;
        while ((d * d) % (4 * k) != 0) {
            d++;
        }
        
        int[][] count = new int[2 * n + 2][d];
        count[n][0] = 1;
        
        int ans = 0;
        int vowels = 0;
        
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                vowels++;
            }
            
            int val = 2 * vowels - (i + 1);
            int rem = (i + 1) % d;
            
            ans += count[val + n][rem];
            count[val + n][rem]++;
        }
        
        return ans;
    }
}