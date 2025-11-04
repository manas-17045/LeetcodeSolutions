// Leetcode 3714: Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/
// Solved on 4th of November, 2025
import java.util.*;

class Solution {
    
    /**
     * Finds the length of the longest balanced substring in a given string.
     * @param s The input string consisting of characters 'a', 'b', and 'c'.
     * @return The length of the longest balanced substring.
     */
    public int longestBalanced(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int maxLen = 1;
        int runLen = 1;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                runLen++;
            } else {
                if (runLen > maxLen) maxLen = runLen;
                runLen = 1;
            }
        }
        if (runLen > maxLen) maxLen = runLen;

        int size = 2 * n + 5;
        int offset = n + 2;
        char[] chars = {'a', 'b', 'c'};
        for (int p = 0; p < 3; p++) {
            char x = chars[p];
            char y = chars[(p + 1) % 3];
            char z = chars[(p + 2) % 3];
            int[] seenIndex = new int[size];
            int[] seenToken = new int[size];
            int token = 1;
            int base = -1;
            int diff = 0;
            seenToken[offset] = token;
            seenIndex[offset] = base;
            for (int i = 0; i < n; i++) {
                char c = s.charAt(i);
                if (c == z) {
                    token++;
                    base = i;
                    diff = 0;
                    seenToken[offset] = token;
                    seenIndex[offset] = base;
                } else {
                    if (c == x) diff++;
                    else if (c == y) diff--;
                    int idx = diff + offset;
                    if (idx < 0) {
                        continue;
                    }
                    if (idx >= size) {
                        continue;
                    }
                    if (seenToken[idx] != token) {
                        seenToken[idx] = token;
                        seenIndex[idx] = i;
                    } else {
                        int len = i - seenIndex[idx];
                        if (len > maxLen) maxLen = len;
                    }
                }
            }
        }

        HashMap<Long, Integer> tripleMap = new HashMap<>(Math.max(16, n * 2));
        int aCount = 0;
        int bCount = 0;
        int cCount = 0;
        tripleMap.put(0L, -1);
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == 'a') aCount++;
            else if (ch == 'b') bCount++;
            else cCount++;
            int diff1 = aCount - bCount;
            int diff2 = aCount - cCount;
            long key = (((long)diff1) << 32) ^ (diff2 & 0xffffffffL);
            Integer first = tripleMap.get(key);
            if (first == null) tripleMap.put(key, i);
            else {
                int len = i - first;
                if (len > maxLen) maxLen = len;
            }
        }
        return maxLen;
    }
}