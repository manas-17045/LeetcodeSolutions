// Leetcode 2644: Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/
// Solved on 2nd of December, 2025
class Solution {
    /**
     * Given two arrays of integers nums and divisors, return the divisor that has the maximum divisibility score.
     * The divisibility score of a divisor is the number of times it divides an element of nums.
     * If there is more than one divisor with the maximum score, return the smallest of them.
     * @param nums The array of numbers.
     * @param divisors The array of divisors.
     * @return The divisor with the maximum divisibility score.
     */
    public int maxDivScore(int[] nums, int[] divisors) {
        int maxScore = -1;
        int result = -1;

        for (int divisor : divisors) {
            int currentScore = 0;
            for (int num : nums) {
                if (num % divisor == 0) {
                    currentScore++;
                }
            }

            if (currentScore > maxScore) {
                maxScore = currentScore;
                result = divisor;
            } else if (currentScore == maxScore) {
                result = Math.min(result, divisor);
            }
        }

        return result;
    }
}