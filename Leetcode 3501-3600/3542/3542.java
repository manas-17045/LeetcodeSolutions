// Leetcode 3542: Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/
// Solved on 10th of November, 2025
import java.util.ArrayDeque;

class Solution {
    /**
     * Calculates the minimum number of operations to convert all elements in the array to zero.
     *
     * @param nums The input array of integers.
     * @return The minimum number of operations required.
     */
    public int minOperations(int[] nums) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int ops = 0;
        for (int num : nums) {
            if (num == 0) {
                stack.clear();
                continue;
            }
            while (!stack.isEmpty() && stack.peekLast() > num) {
                stack.removeLast();
            }
            if (stack.isEmpty() || stack.peekLast() < num) {
                stack.addLast(num);
                ops++;
            }
        }
        return ops;
    }
}