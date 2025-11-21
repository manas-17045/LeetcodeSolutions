// Leetcode 3747: Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/
// Solved on 21st of November, 2025
class Solution {
    /**
     * Counts the number of distinct integers after removing zeros.
     * @param n The input long integer.
     * @return The count of distinct integers.
     */
    public long countDistinct(long n) {
        String numString = Long.toString(n);
        int length = numString.length();
        long count = 0;
        long power = 1;

        for (int i = 1; i < length; i++) {
            power *= 9;
            count += power;
        }

        for (int i = 0; i < length; i++) {
            int digit = numString.charAt(i) - '0';
            if (digit > 1) {
                count += (digit - 1) * power;
            }
            if (digit == 0) {
                return count;
            }
            power /= 9;
        }

        return count + 1;
    }
}