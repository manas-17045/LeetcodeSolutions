// Leetcide 2283: Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
// Solved on 7th of March, 2026
class Solution {
    /**
     * Checks if for every index i in the string, the digit at index i 
     * is equal to the number of times the digit i appears in the string.
     * 
     * @param num A string of digits.
     * @return True if the condition holds for all indices, false otherwise.
     */
    public boolean digitCount(String num) {
        int[] frequency = new int[10];
        int length = num.length();

        for ( int i = 0; i < length; i++) {
            frequency[num.charAt(i) - '0']++;
        }

        for (int i = 0; i < length; i++) {
            if (frequency[i] != num.charAt(i) - '0') {
                return false;
            }
        }
        
        return true;
    }
}