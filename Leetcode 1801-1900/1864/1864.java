// leetcode 1864: Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
// Solved on 25th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of swaps required to make a binary string alternating.
     * An alternating binary string is one where no two adjacent characters are the same (e.g., "01010" or "10101").
     * @param s The input binary string.
     * @return The minimum number of swaps needed, or -1 if it's impossible to make the string alternating.
     */
    public int minSwaps(String s) {
        int n = s.length();
        int zeros = 0;
        int ones = 0;
        int mismatches = 0;

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '0') {
                zeros++;
            } else {
                ones++;
            }

            if (i % 2 == 0 && c == '1') {
                mismatches++;
            } else if (i % 2 == 1 && c == '0') {
                mismatches++;
            }
        }

        if (Math.abs(zeros - ones) > 1) {
            return -1;
        }

        if (zeros > ones) {
            return mismatches / 2;
        } else if (ones > zeros) {
            return (n - mismatches) / 2;
        } else {
            return Math.min(mismatches, n - mismatches) / 2;
        }
    }
}