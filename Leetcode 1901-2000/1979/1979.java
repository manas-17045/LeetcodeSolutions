// Leetcode 1979: Find Greatest Common Divisor of Array
// https://leetcode.com/problems/find-greatest-common-divisor-of-array/
// Solved on 18th of July, 2026
class Solution {
    /**
     * Finds the greatest common divisor of the smallest and largest numbers in the array.
     * 
     * @param nums the input array of integers
     * @return the greatest common divisor of the smallest and largest numbers in the array
     */
    public int findGCD(int[] nums) {
        int minVal = nums[0];
        int maxVal = nums[0];
        for (int num : nums) {
            if (num < minVal) {
                minVal = num;
            }
            if (num > maxVal) {
                maxVal = num;
            }
        }
        return getGcd(minVal, maxVal);
    }

    private int getGcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}