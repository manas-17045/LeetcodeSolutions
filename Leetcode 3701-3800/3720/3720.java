// Leetcode 3720: Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/
// Solved on 30th of October, 2025
class Solution {
    /**
     * Finds the lexicographically smallest permutation of string `s` that is greater than string `target`.
     * @param s The input string from which to form a permutation.
     * @param target The target string to compare against.
     * @return The lexicographically smallest permutation of `s` that is greater than `target`, or an empty string if no such permutation exists.
     */
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();
        int[] charCounts = new int[26];
        for (char c : s.toCharArray()) {
            charCounts[c - 'a']++;
        }
        char[] result = new char[n];

        if (solve(0, charCounts, target, result, false)) {
            return new String(result);
        }
        return "";
    }

    private boolean solve(int index, int[] charCounts, String target, char[] result, boolean isGreater) {
        if (index == target.length()) {
            return isGreater;
        }

        if (isGreater) {
            fillRest(index, charCounts, result);
            return true;
        }

        int targetChar = target.charAt(index) - 'a';

        if (charCounts[targetChar] > 0) {
            result[index] = (char)('a' + targetChar);
            charCounts[targetChar]--;
            if (solve(index + 1, charCounts, target, result, false)) {
                return true;
            }
            charCounts[targetChar]++;
        }

        for (int i = targetChar + 1; i < 26; i++) {
            if (charCounts[i] > 0) {
                result[index] = (char)('a' + i);
                charCounts[i]--;
                fillRest(index + 1, charCounts, result);
                return true;
            }
        }

        return false;
    }

    private void fillRest(int index, int[] charCounts, char[] result) {
        int charCode = 0;
        for (int i = index; i < result.length; i++) {
            while (charCounts[charCode] == 0) {
                charCode++;
            }
            result[i] = (char)('a' + charCode);
            charCounts[charCode]--;
        }
    }
}