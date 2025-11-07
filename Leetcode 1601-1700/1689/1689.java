// Leetcode 1689: Partitioning Into Minimum Number of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
// Solved on 7th of November, 2025
class Solution {
    /**
     * Given a decimal string n, return the minimum number of positive deci-binary numbers needed to sum up to n.
     * @param n The decimal string.
     * @return The minimum number of positive deci-binary numbers.
     */
    public int minPartitions(String n) {
        int maxDigit = 0;
        for (int i = 0; i < n.length(); i++) {
            int digit = n.charAt(i) - '0';
            if (digit > maxDigit) {
                maxDigit = digit;
                if (maxDigit == 9) {
                    break;
                }
            }
        }
        return maxDigit;
    }
}