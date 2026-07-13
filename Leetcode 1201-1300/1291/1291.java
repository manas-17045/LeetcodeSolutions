// Leetcode 1291: Sequential Digits
// https://leetcode.com/problems/sequential-digits/
// Solved on 13th of July, 2026
class Solution {
    /**
     * Finds all sequential digits in the range of low and high
     * A sequential digit number is a number that has digits in increasing order
     * e.g., 12, 123, 1234, etc.
     * 
     * @param low  the lower bound of the range
     * @param high the upper bound of the range
     * @return a list of sequential digits in the range
     */
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> result = new ArrayList<>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 1; start <= 10 - length; start++) {
                int num = 0;
                for (int i = 0; i < length; i++) {
                    num = num * 10 + (start + i);
                }
                if (num >= low && num <= high) {
                    result.add(num);
                }
            }
        }
        return result;
    }
}