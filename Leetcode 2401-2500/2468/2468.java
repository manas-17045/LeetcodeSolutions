// Leetcode 2468: Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/
// Solved on 15th of November, 2025
class Solution {
    /**
     * Splits a given message into parts, each limited by a specified length.
     * @param message The original message string.
     * @param limit The maximum length of each part, including the suffix.
     * @return An array of strings representing the split message, or an empty array if no valid split is possible.
     */
    public String[] splitMessage(String message, int limit) {
        int n = message.length();
        for (int k = 1; k <= n; k++) {
            int dk = numDigits(k);
            long totalDigitsI = 0;
            long pow = 1;
            for (int d = 1; d <= dk; d++) {
                long start = pow;
                long end = Math.min(k, (int)(pow * 10 - 1));
                if (start > end) {
                    pow *= 10;
                    continue;
                }
                totalDigitsI += (end - start + 1) * (long)d;
                pow *= 10;
            }
            long totalSuffix = totalDigitsI + (long)k * dk + 3L * k;
            long totalContentCapacity = (long)k * limit - totalSuffix;
            if (totalContentCapacity < n) {
                continue;
            }
            String[] parts = new String[k];
            int pos = 0;
            boolean ok = true;
            for (int i = 1; i <= k; i++) {
                int si = numDigits(i);
                int cap = limit - (si + dk + 3);
                if (cap < 0) {
                    ok = false;
                    break;
                }
                int take = Math.min(cap, n - pos);
                StringBuilder sb = new StringBuilder();
                if (take > 0) {
                    sb.append(message, pos, pos + take);
                    pos += take;
                }
                sb.append('<').append(i).append('/').append(k).append('>');
                parts[i - 1] = sb.toString();
            }
            if (!ok) {
                continue;
            }
            if (pos == n) {
                return parts;
            }
        }
        return new String[0];
    }
    private int numDigits(int x) {
        if (x >= 1000000000) {
            return 10;
        }
        if (x >= 100000000) {
            return 9;
        }
        if (x >= 10000000) {
            return 8;
        }
        if (x >= 1000000) {
            return 7;
        }
        if (x >= 100000) {
            return 6;
        }
        if (x >= 10000) {
            return 5;
        }
        if (x >= 1000) {
            return 4;
        }
        if (x >= 100) {
            return 3;
        }
        if (x >= 10) {
            return 2;
        }
        return 1;
    }
}