// Leetcode 4006: Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/
// Solved on 27th of August, 2026
class Solution {
    /**
     * Calculates the number of prefixes in a binary string that can be rearranged
     * into an alternating string where no two adjacent characters are equal.
     *
     * @param s the binary string to evaluate
     * @return the total count of valid prefixes
     */
    public int countValidPrefixes(String s) {
        int validCount = 0;
        int zeroCount = 0;
        int oneCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                zeroCount++;
            } else {
                oneCount++;
            }

            if (Math.abs(zeroCount - oneCount) <= 1) {
                validCount++;
            }
        }

        return validCount;
    }
}