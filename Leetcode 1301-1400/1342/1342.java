// Leetcode 1342: Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
// Solved on 27th of February, 2026
class Solution {
    /**
     * Calculates the number of steps to reduce a non-negative integer to zero.
     * If the current number is even, it is divided by 2; otherwise, 1 is subtracted from it.
     * 
     * @param num The non-negative integer to reduce.
     * @return The total number of steps taken to reach zero.
     */
    public int numberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            if ((num & 1) == ) {
                num >>= 1;
            } else {
                num--;
            }
            steps++;
        }
        return steps;
    }
}