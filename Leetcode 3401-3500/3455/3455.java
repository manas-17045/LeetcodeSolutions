// Leetcode 3455: Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/
// Solved on 30th of November, 2025
import java.util.*;

class Solution {
    /**
     * Finds the length of the shortest substring in `s` that matches the pattern `p`.
     * The pattern `p` can contain at most two '*' characters, splitting it into three parts.
     * @param s The main string to search within.
     * @param p The pattern string, which can contain '*' as a wildcard.
     * @return The length of the shortest matching substring, or -1 if no such substring exists.
     */
    public int shortestMatchingSubstring(String s, String p) {
        int n = s.length();
        String[] parts = p.split("\\*", -1);
        String p1 = parts[0];
        String p2 = parts[1];
        String p3 = parts[2];

        List<Integer> m1 = p1.isEmpty() ? new ArrayList<>() : kmp(s, p1);
        List<Integer> m2 = p2.isEmpty() ? new ArrayList<>() : kmp(s, p2);
        List<Integer> m3 = p3.isEmpty() ? new ArrayList<>() : kmp(s, p3);

        if (!p1.isEmpty() && m1.isEmpty()) {
            return -1;
        }
        if (!p2.isEmpty() && m2.isEmpty()) {
            return -1;
        }
        if (!p3.isEmpty() && m3.isEmpty()) {
            return -1;
        }

        int[] prev1 = new int[n + 1];
        Arrays.fill(prev1, -1);
        if (!p1.isEmpty()) {
            int idx = 0;
            int last = -1;
            for (int i = 0; i <= n; i++) {
                while (idx < m1.size() && m1.get(idx) + p1.length() <= i) {
                    last = m1.get(idx);
                    idx++;
                }
                prev1[i] = last;
            }
        }

        int[] next3 = new int[n + 1];
        Arrays.fill(next3, -1);
        if (!p3.isEmpty()) {
            int idx = m3.size() - 1;
            int last = -1;
            for (int i = n; i >= 0; i--) {
                while (idx >= 0 && m3.get(idx) >= i) {
                    last = m3.get(idx);
                    idx--;
                }
                next3[i] = last;
            }
        }

        int minLen = Integer.MAX_VALUE;
        boolean has1 = !p1.isEmpty();
        boolean has2 = !p2.isEmpty();
        boolean has3 = !p3.isEmpty();

        if (has2) {
            for (int k : m2) {
                int start = k;
                if (has1) {
                    start = prev1[k];
                    if (start == -1) {
                        continue;
                    }
                }
                int end = k + p2.length();
                if (has3) {
                    int m = next3[k + p2.length()];
                    if (m == -1) {
                        continue;
                    }
                    end = m + p3.length();
                }
                minLen = Math.min(minLen, end - start);
            }
        } else {
            if (has1 && has3) {
                for (int m : m3) {
                    int i = prev1[m];
                    if (i != -1) {
                        minLen = Math.min(minLen, m + p3.length() - i);
                    }
                }
            } else if (has1) {
                minLen = p1.length();
            } else if (has3) {
                minLen = p3.length();
            } else {
                minLen = 0;
            }
        }

        return minLen == Integer.MAX_VALUE ? -1 : minLen;
    }

    private List<Integer> kmp(String s, String p) {
        List<Integer> res = new ArrayList<>();
        int n = s.length();
        int m = p.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        while (i < m) {
            if (p.charAt(i) == p.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        int j = 0;
        i = 0;
        while (i < n) {
            if (p.charAt(j) == s.charAt(i)) {
                j++;
                i++;
            }
            if (j == m) {
                res.add(i - j);
                j = lps[j - 1];
            } else if (i < n && p.charAt(j) != s.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return res;
    }
}