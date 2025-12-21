// Leetcode 3734: Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
// Solved on 21st of December, 2025
class Solution {
    /**
     * Finds the lexicographically smallest palindromic permutation of string `s` that is strictly greater than string `target`.
     * @param s The input string from which to form a palindromic permutation.
     * @param target The target string to compare against.
     * @return The lexicographically smallest palindromic permutation of `s` that is greater than `target`,
     *         or an empty string if no such permutation exists.
     */
    public String lexPalindromicPermutation(Strng s, String target) {
        int n = s.length();
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        int oddCount = 0;
        Character mid = null;
        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 != 0) {
                oddCount++;
                mid = (char) ('a' + i);
            }
        }

        if (oddCount > 1) {
            return "";
        }

        int[] halfCount = new int[26];
        for (int i = 0; i < 26; i++) {
            halfCount[i] = count[i] / 2;
        }

        int m = n / 2;
        char[] currentHalf = new char[m];
        int matchLen = 0;

        for (int i = 0; i < m; i++) {
            char c = target.charAt(i);
            if (halfCount[c - 'a'] > 0) {
                halfCount[c - 'a']--;
                currentHalf[i] = c;
                matchLen++;
            } else {
                break;
            }
        }

        int startI = matchLen;

        if (matchLen == m) {
            String candidate = buildPalindrome(currentHalf, mid);
            if (candidate.compareTo(target) > 0) {
                return candidate;
            }
            if (m == 0) {
                return "";
            }
            startI = m - 1;
            halfCount[currentHalf[startI] - 'a']++;
        }

        for (int i = startI; i >= 0; i--) {
            char targetChar = target.charAt(i);
            for (int c = targetChar - 'a' + 1; c < 26; c++) {
                if (halfCount[c] > 0) {
                    halfCount[c]--;
                    currentHalf[i] = (char) ('a' + c);
                    fillRemaining(currentHalf, halfCount, i + 1);
                    return buildPalindrome(currentHalf, mid);
                }
            }
            if (i > 0) {
                halfCount[currentHalf[i - 1] - 'a']++;
            }
        }

        return "";
    }

    private void fillRemaining(char[] half, int[] counts, int start) {
        for (int i = start; i < half.length; i++) {
            for (int c = 0; c < 26; c++) {
                if (counts[c] > 0) {
                    counts[c]--;
                    half[i] = (char) ('a' + c);
                    break;
                }
            }
        }
    }

    private String buildPalindrome(char[] half, Character mid) {
        StringBuilder sb = new StringBuilder();
        sb.append(half);
        String first = sb.toString();
        String rev = sb.reverse().toString();
        if (mid != null) {
            return first + mid + rev;
        }
        return first + rev;
    }
}