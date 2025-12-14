// Leetcode 3448: Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/
// Solved on 14th of December, 2025
class Solution {
    /**
     * Counts the number of substrings in a given string `s` that are divisible by their last digit.
     *
     * @param s The input string consisting of digits.
     * @return The total count of such substrings.
     */
    pub;ic long countSubstrings(String s) {
        long ans = 0;
        int n = s.length();
        int[] count3 = new int[3];
        int[] count9 = new int[9];
        int[] count7 = new int[7];
        
        count3[0] = 1;
        count9[0] = 1;
        count7[0] = 1;
        
        int r3 = 0, r9 = 0, r7 = 0;
        int[] inv7 = {1, 5, 4, 6, 2, 3};
        
        for (int i = 0; i < n; i++) {
            int d = s.charAt(i) - '0';
            r3 = (r3 + d) % 3;
            r9 = (r9 + d) % 9;
            r7 = (r7 * 10 + d) % 7;
            
            if (d != 0) {
                if (d == 1 || d == 2 || d == 5) {
                    ans += (i + 1);
                } else if (d == 3 || d == 6) {
                    ans += count3[r3];
                } else if (d == 9) {
                    ans += count9[r9];
                } else if (d == 4) {
                    ans++;
                    if (i >= 1) {
                        int val = (s.charAt(i - 1) - '0') * 10 + d;
                        if (val % 4 == 0) ans += i;
                    }
                } else if (d == 8) {
                    ans++;
                    if (i >= 1) {
                        int val = (s.charAt(i - 1) - '0') * 10 + d;
                        if (val % 8 == 0) ans++;
                    }
                    if (i >= 2) {
                        int val = (s.charAt(i - 2) - '0') * 100 + (s.charAt(i - 1) - '0') * 10 + d;
                        if (val % 8 == 0) ans += (i - 1);
                    }
                } else if (d == 7) {
                    int key = (r7 * inv7[i % 6]) % 7;
                    ans += count7[key];
                }
            }
            
            count3[r3]++;
            count9[r9]++;
            int key7 = (r7 * inv7[i % 6]) % 7;
            count7[key7]++;
        }
        
        return ans;
    }
}