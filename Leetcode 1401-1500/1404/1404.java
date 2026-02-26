// Leetcode 1404: Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
// Solved on 26th of February, 2026
class Solution {
    /**
     * Calculates the number of steps to reduce a binary string to "1".
     * If the number is even, divide it by 2 (shift right).
     * If the number is odd, add 1 to it.
     *
     * @param s The binary representation of a positive integer.
     * @return The total number of steps required to reach 1.
     */
    public int numSteps(String s) {
        int stepCount = 0;
        int carryBit = 0;

        for (int i = s.length() - 1; i > 0; i--) {
            int currentDigit = s.charAt(i) - '0' + carryBit;

            if (currentDigit % 2 == 1) {
                stepCount += 2;
                carryBit = 1;
            } else {
                stepCount += 1;
            }
        }

        return stepCount + carryBit;
    }
}