// Leetcode 3474: Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/
// Solved on 31st of March, 2026
class Solution {
    /**
     * Generates the lexicographically smallest string res such that str1[i] is 'T' if 
     * res.substring(i, i + m) equals str2, and 'F' otherwise.
     *
     * @param str1 A string of 'T' and 'F' representing the required match results.
     * @param str2 The pattern string to match against.
     * @return The lexicographically smallest valid string, or an empty string if none exists.
     */
    public String generatedString(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int len = n + m - 1;
        char[] res = new char[len];
        for (int i = 0; i < len; i++) {
            res[i] = '?';
        }
        
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; j++) {
                    if (res[i + j] != '?' && res[i + j] != str2.charAt(j)) {
                        return "";
                    }
                    res[i + j] = str2.charAt(j);
                }
            }
        }
        
        int[] qCount = new int[n];
        int[] matchCount = new int[n];
        int[] fCount = new int[len];
        
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'F') {
                for (int j = 0; j < m; j++) {
                    int k = i + j;
                    if (res[k] == '?') {
                        qCount[i]++;
                        fCount[k]++;
                    } else if (res[k] == str2.charAt(j)) {
                        matchCount[i]++;
                    }
                }
                if (qCount[i] == 0 && matchCount[i] == m) {
                    return "";
                }
            }
        }
        
        int[][] fCovering = new int[len][];
        for (int i = 0; i < len; i++) {
            fCovering[i] = new int[fCount[i]];
        }
        
        int[] fIdx = new int[len];
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'F') {
                for (int j = 0; j < m; j++) {
                    int k = i + j;
                    if (res[k] == '?') {
                        fCovering[k][fIdx[k]++] = i;
                    }
                }
            }
        }
        
        int qTotal = 0;
        for (int i = 0; i < len; i++) {
            if (res[i] == '?') {
                qTotal++;
            }
        }
        
        int[] qs = new int[qTotal];
        int qIndex = 0;
        for (int i = 0; i < len; i++) {
            if (res[i] == '?') {
                qs[qIndex++] = i;
            }
        }
        
        int[] choice = new int[qTotal];
        for (int i = 0; i < qTotal; i++) {
            choice[i] = -1;
        }
        
        int idx = 0;
        while (idx >= 0 && idx < qTotal) {
            int k = qs[idx];
            
            if (choice[idx] != -1) {
                char prevC = (char) ('a' + choice[idx]);
                for (int i : fCovering[k]) {
                    qCount[i]++;
                    if (prevC == str2.charAt(k - i)) {
                        matchCount[i]--;
                    }
                }
            }
            
            int forbiddenMask = 0;
            for (int i : fCovering[k]) {
                if (qCount[i] == 1 && matchCount[i] == m - 1) {
                    forbiddenMask |= (1 << (str2.charAt(k - i) - 'a'));
                }
            }
            
            boolean found = false;
            for (int cInt = choice[idx] + 1; cInt < 26; cInt++) {
                if ((forbiddenMask & (1 << cInt)) == 0) {
                    choice[idx] = cInt;
                    char c = (char) ('a' + cInt);
                    res[k] = c;
                    
                    for (int i : fCovering[k]) {
                        qCount[i]--;
                        if (c == str2.charAt(k - i)) {
                            matchCount[i]++;
                        }
                    }
                    found = true;
                    break;
                }
            }
            
            if (found) {
                idx++;
            } else {
                choice[idx] = -1;
                res[k] = '?';
                idx--;
            }
        }
        
        if (idx < 0) {
            return "";
        }
        
        return new String(res);
    }
}