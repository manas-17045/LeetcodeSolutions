// Leetcode 2710: Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
// Solved on 7th of December, 2025
class Solution {
    /**
     * Removes all trailing zeros from a string representation of a non-negative integer.
     *
     * @param num The input string representing a non-negative integer.
     * @return The string with all trailing zeros removed.
     */
    public String removeTrailingZeros(String num){
        int index = num.length() - 1;
        while (index >= 0 && num.charAt(index) == '0') {
            index--;
        }
        return num.substring(0, index + 1);
    }
}