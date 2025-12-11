// Leetcode 3008: Find Beautiful Indices in the Given Array II
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/description/
// Solved on 11th of December, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Finds "beautiful" indices in a given string `s`.
     * An index `i` is beautiful if `s[i...i+a.length()-1]` equals `a`, and there exists an index `j` such that
     * `s[j...j+b.length()-1]` equals `b`, and `|i - j| <= k`.
     * @param s The main string to search within.
     * @param a The first pattern string.
     * @param b The second pattern string.
     * @param k The maximum allowed absolute difference between indices `i` and `j`.
     * @return A list of all beautiful indices `i`.
     */
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        List<Integer> indicesA = kmpSearch(s, a);
        List<Integer> indicesB = kmpSearch(s, b);
        List<Integer> result = new ArrayList<>();

        int j = 0;
        for (int i : indicesA) {
            while (j < indicesB.size() && indicesB.get(j) < i - k) {
                j++;
            }
            if (j < indicesB.size() && Math.abs(indicesB.get(j) - i) <= k) {
                result.add(i);
            }
        }
        return result;
    }

    private List<Integer> kmpSearch(String text, String pattern) {
        List<Integer> foundIndices = new ArrayList<>();
        int n = text.length();
        int m = pattern.length();
        if (m > n) {
            return foundIndices;
        }

        int[] lps = computeLPS(pattern);
        int i = 0;
        int j = 0;
        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                j++;
                i++;
            }
            if (j == m) {
                foundIndices.add(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return foundIndices;
    }

    private int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int length = 0;
        int i = 1;
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
}