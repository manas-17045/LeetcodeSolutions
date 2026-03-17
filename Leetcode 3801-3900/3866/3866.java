// Leetcode 3866: First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/
// Solved on 17th of March, 2026
class Solution {
    /**
     * Finds the first even element in the array that appears exactly once.
     * 
     * @param nums An array of integers.
     * @return The first unique even integer found, or -1 if none exist.
     */
    public int firstUniqueEven(int[] nums) {
        int[] counts = new int[101];
        for (int num : nums) {
            counts[num]++;
        }
        for (int num : nums) {
            if (num % 2 == 0 && counts[num] == 1) {
                return num;
            }
        }
        return -1;
    }
}