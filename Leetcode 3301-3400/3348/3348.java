// Leetcode 3348: Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/
// Solved on 26th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds the smallest number (as a string) that is greater than or equal to `num`
     * and whose digit product is divisible by `t`.
     * @param num The input number as a string.
     * @param t The divisor for the digit product.
     * @return The smallest number as a string, or "-1" if no such number exists.
     */
    public String smallestNumber(String num, long t) {
        long tempT = t;
        int[] tCounts = new int[10];
        for (int i : new int[]{2, 3, 5, 7}) {
            while (tempT % i == 0) {
                tCounts[i]++;
                tempT /= i;
            }
        }
        if (tempT > 1) {
            return "-1";
        }

        int n = num.length();
        int firstZero = -1;
        for (int i = 0; i < n; i++) {
            if (num.charAt(i) == '0') {
                firstZero = i;
                break;
            }
        }

        int[] pCounts = new int[10];
        if (firstZero == -1) {
            boolean ok = true;
            for (char c : num.toCharArray()) {
                int d = c - '0';
                for (int k : new int[]{2, 3, 5, 7}) {
                    while (d > 0 && d % k == 0) {
                        pCounts[k]++;
                        d /= k;
                    }
                }
            }
            for (int k : new int[]{2, 3, 5, 7}) {
                if (pCounts[k] < tCounts[k]) {
                    ok = false;
                }
            }
            if (ok) {
                return num;
            }
        }

        pCounts = new int[10];
        int limit = (firstZero == -1) ? n - 1 : firstZero;
        for (int i = 0; i < limit; i++) {
            int d = num.charAt(i) - '0';
            for (int k : new int[]{2, 3, 5, 7}) {
                while (d > 0 && d % k == 0) {
                    pCounts[k]++;
                    d /= k;
                }
            }
        }

        for (int i = limit; i >= 0; i--) {
            int startDigit = (num.charAt(i) - '0') + 1;
            for (int d = startDigit; d <= 9; d++) {
                int[] currentCounts = pCounts.clone();
                int tempD = d;
                for (int k : new int[]{2, 3, 5, 7}) {
                    while (tempD > 0 && tempD % k == 0) {
                        currentCounts[k]++;
                        tempD /= k;
                    }
                }

                int remLen = n - 1 - i;
                String suffix = getSuffix(remLen, tCounts, currentCounts);
                if (suffix != null) {
                    return num.substring(0, i) + d + suffix;
                }
            }

            if (i > 0) {
                int prevD = num.charAt(i - 1) - '0';
                for (int k : new int[]{2, 3, 5, 7}) {
                    while (prevD > 0 && prevD % k == 0) {
                        pCounts[k]--;
                        prevD /= k;
                    }
                }
            }
        }

        for (int len = n + 1; ; len++) {
            String suffix = getSuffix(len, tCounts, new int[10]);
            if (suffix != null) {
                return suffix;
            }
        }
    }

    private String getSuffix(int len, int[] tCounts, int[] currentCounts) {
        int[] needed = new int[10];
        for (int k : new int[]{2, 3, 5, 7}) {
            needed[k] = Math.max(0, tCounts[k] - currentCounts[k]);
        }

        StringBuilder sb = new StringBuilder();
        while (needed[7] > 0) {
            sb.append(7);
            needed[7]--;
        }
        while (needed[5] > 0) {
            sb.append(5);
            needed[5]--; 
        }
        while (needed[3] >= 2) {
            sb.append(9);
            needed[3] -= 2;
        }
        while (needed[2] >= 3) {
            sb.append(8);
            needed[2] -= 3;
        }
        while (needed[3] >= 1 && needed[2] >= 1) {
            sb.append(6);
            needed[3]--;
            needed[2]--;
        }
        while (needed[2] >= 2) {
            sb.append(4);
            needed[2] -= 2;
        }
        while (needed[3] > 0) {
            sb.append(3);
            needed[3]--;
        }
        while (needed[2] > 0) {
            sb.append(2);
            needed[2]--;
        }

        if (sb.length() > len) {
            return null;
        }

        char[] chars = new char[sb.length()];
        sb.getChars(0, sb.length(), chars, 0);
        Arrays.sort(chars);

        StringBuilder res = new StringBuilder();
        for (int k = 0; k < len - sb.length(); k++) {
            res.append('1');
        }
        res.append(chars);
        return res.toString();
    }
}