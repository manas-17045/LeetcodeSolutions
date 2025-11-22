// Leetcode 2593: Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
// Solved on 22nd of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the score of an array after marking elements.
     * @param nums The input array of integers.
     * @return The total score.
     */
    public long findScore(int[] nums) {
        int n = nums.length;
        long[] elements = new long[n];
        for (int i = 0; i < n; i++) {
            elements[i] = ((long) nums[i] << 32) | i;
        }
        Arrays.sort(elements);
        boolean[] marked = new boolean[n];
        long score = 0;
        for (long element : elements) {
            int index = (int) element;
            if (!marked[index]) {
                score += (element >> 32);
                marked[index] = true;
                if (index > 0) {
                    marked[index - 1] = true;
                }
                if (index < n - 1) {
                    marked[index + 1] = true;
                }
            }
        }
        return score;
    }
}