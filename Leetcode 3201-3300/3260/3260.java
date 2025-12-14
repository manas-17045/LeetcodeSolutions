// Leetcode 3260: Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/
// Solved on 14th of December, 2025
class Solution {
    /**
     * Given an integer n and an integer k, return the largest palindrome of length n that is divisible by k.
     * @param n The length of the palindrome.
     * @param k The divisor.
     * @return The largest palindrome of length n that is divisible by k.
     */
    public String largestPalindrome(int n, int k) {
        char[] ans = new char[n];
        for (int i = 0; i < n; i++) {
            ans[i] = '9';
        }

        if (k == 1 || k == 3 || k == 9) {
            return new String(ans);
        }

        if (k == 2) {
            ans[0] = '8';
            ans[n - 1] = '8';
            return new String(ans);
        }

        if (k == 4) {
            ans[0] = '8';
            ans[n - 1] = '8';
            if (n > 2) {
                ans[1] = '8';
                ans[n - 2] = '8';
            }
            return new String(ans);
        }

        if (k == 5) {
            ans[0] = '5';
            ans[n - 1] = '5';
            return new String(ans);
        }

        if (k == 6) {
            if (n == 1) return "6";
            if (n == 2) return "66";
            ans[0] = '8';
            ans[n - 1] = '8';
            if (n % 2 == 1) {
                ans[n / 2] = '8';
            } else {
                ans[n / 2] = '7';
                ans[n / 2 - 1] = '7';
            }
            return new String(ans);
        }

        if (k == 8) {
            ans[0] = '8';
            ans[n - 1] = '8';
            if (n > 2) {
                ans[1] = '8';
                ans[n - 2] = '8';
            }
            if (n > 4) {
                ans[2] = '8';
                ans[n - 3] = '8';
            }
            return new String(ans);
        }

        if (k == 7) {
            for (char d = '9'; d >= '0'; d--) {
                if (n % 2 == 1) {
                    ans[n / 2] = d;
                } else {
                    ans[n / 2] = d;
                    ans[n / 2 - 1] = d;
                }
                int rem = 0;
                for (char c : ans) {
                    rem = (rem * 10 + (c - '0')) % 7;
                }
                if (rem == 0) {
                    return new String(ans);
                }
            }
        }

        return new String(ans);
    }
}