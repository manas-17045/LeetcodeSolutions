// Leetcode 3518: Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
// Solved on 6th of December, 2025
import java.math.BigInteger;

class Solution {
    /**
     * Given a string `s` and an integer `k`, return the k-th lexicographically smallest palindromic rearrangement of `s`.
     * @param s The input string.
     * @param k The k-th smallest palindromic rearrangement to find.
     * @return The k-th lexicographically smallest palindromic rearrangement of `s`.
     */
    public String smallestPalindrome(String s, int k) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        String mid = "";
        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 == 1) {
                if (!mid.isEmpty()) {
                    return "";
                }
                mid = String.valueOf((char) ('a' + i));
            }
            count[i] /= 2;
        }

        int n = s.length() / 2;
        double[] logFact = new double[n + 1];
        for (int i = 2; i <= n; i++) {
            logFact[i] = logFact[i - 1] + Math.log(i);
        }

        long kLong = k;
        StringBuilder half = new StringBuilder();

        for (int i = 0; i < n; i++) {
            boolean picked = false;
            int remainingLen = n - 1 - i;

            for (int j = 0; j < 26; j++) {
                if (count[j] == 0) {
                    continue;
                }

                count[j]--;

                double currentLogDenom = 0;
                for (int c = 0; c < 26; c++) {
                    currentLogDenom += logFact[count[c]];
                }
                double logPerm = logFact[remainingLen] - currentLogDenom;

                if (logPerm > 25.0) {
                    picked = true;
                    half.append((char) ('a' + j));
                    break;
                }

                int maxVal = -1;
                int maxIdx = -1;
                for (int x = 0; x < 26; x++) {
                    if (count[x] > maxVal) {
                        maxVal = count[x];
                        maxIdx = x;
                    }
                }

                BigInteger num = BigInteger.ONE;
                for (int x = maxVal + 1; x <= remainingLen; x++) {
                    num = num.multiply(BigInteger.valueOf(x));
                }

                BigInteger den = BigInteger.ONE;
                for (int x = 0; x < 26; x++) {
                    if (x == maxIdx) {
                        continue;
                    }
                    if (count[x] > 1) {
                        BigInteger term = BigInteger.ONE;
                        for (int y = 2; y <= count[x]; y++) {
                            term = term.multiply(BigInteger.valueOf(y));
                        }
                        den = den.multiply(term);
                    }
                }

                BigInteger ways = num.divide(den);

                if (ways.compareTo(BigInteger.valueOf(kLong)) >= 0) {
                    picked = true;
                    half.append((char) ('a' + j));
                    break;
                } else {
                    kLong -= ways.longValue();
                    count[j]++;
                }
            }
            if (!picked) {
                return "";
            }
        }

        return half.toString() + mid + half.reverse().toString();
    }
}