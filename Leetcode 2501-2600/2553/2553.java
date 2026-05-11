// Leetcode 2553: Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/
// Solved on 11th of May, 2026
class Solution {
    /**
     * Separates each number in the input array into its individual digits.
     * @param nums An array of positive integers.
     * @return An array containing the digits of each number in the original order.
     */
    public int[] separateDigits(int[] nums) {
        int totalDigits = 0;
        for (int i = 0; i < nums.length; i++) {
            int currentNumber = nums[i];
            while (currentNumber > 0) {
                totalDigits++;
                currentNumber /= 10;
            }
        }
        
        int[] answer = new int[totalDigits];
        int index = totalDigits - 1;
        
        for (int i = nums.length - 1; i >= 0; i--) {
            int currentNumber = nums[i];
            while (currentNumber > 0) {
                answer[index] = currentNumber % 10;
                currentNumber /= 10;
                index--;
            }
        }
        
        return answer;
    }
}