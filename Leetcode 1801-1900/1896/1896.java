// Leetcode 1896: Minimum Cost to Change the Final value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
// Solved on 22nd of November, 2025
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    /**
     * Calculates the minimum number of operations to flip the final value of a boolean expression.
     * @param expression The boolean expression as a string.
     * @return The minimum number of operations required.
     */
    public int minOperationsToFlip(String expression) {
        Deque<int[]> nums = new ArrayDeque<>();
        Deque<Character> ops = new ArrayDeque<>();

        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);
            if (c == '(') {
                ops.push(c);
            } else if (c == ')') {
                while (ops.peek() != '(') {
                    eval(nums, ops);
                }
                ops.pop();
            } else if (c == '&' || c == '|') {
                while (!ops.isEmpty() && ops.peek() != '(') {
                    eval(nums, ops);
                }
                ops.push(c);
            } else {
                nums.push(c == '0' ? new int[]{0, 1} : new int[]{1, 0});
            }
        }

        while (!ops.isEmpty()) {
            eval(nums, ops);
        }

        return Math.max(nums.peek()[0], nums.peek()[1]);
    }

    private void eval(Deque<int[]> nums, Deque<Character> ops) {
        char op = ops.pop();
        int[] r = nums.pop();
        int[] l = nums.pop();
        
        if (op == '&') {
            nums.push(new int[]{
                Math.min(l[0], r[0]),
                Math.min(l[1] + r[1], Math.min(l[1], r[1]) + 1)
            });
        } else {
            nums.push(new int[]{
                Math.min(l[0] + r[0], Math.min(l[0], r[0]) + 1),
                Math.min(l[1], r[1])
            });
        }
    }
}