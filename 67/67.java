// Leetcode 67: Add Binary
// https://leetcode.com/problems/add-binary/
// Solved on 15th of February, 2026
class Solution {
    /**
     * Adds two binary strings and returns their sum as a binary string.
     *
     * @param a The first binary string.
     * @param b The second binary string.
     * @return The sum of the two binary strings.
     */
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;
            if (i >= 0) {
                sum += a.charAt(i) - '0';
                i--;
            }
            if (j >= 0) {
                sum += b.charAt(j) - '0';
                j--;
            }
            result.append(sum % 2);
            carry = sum / 2;
        }

        return result.reverse().toString();
    }
}