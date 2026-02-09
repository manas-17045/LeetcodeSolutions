// Leetcode 3834: Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/
// Solved on 9th of February, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Merges adjacent equal elements in an array by summing them up repeatedly.
     * @param nums The input array of integers.
     * @return A list of Longs representing the final state after all possible merges.
     */
    public List<Long> mergeAdjacent(int[] nums) {
        List<Long> stack = new ArrayList<>();
        for (int num : nums) {
            long current = num;
            while (!stack.isEmpty() && stack.get(stack.size() - 1) == current) {
                current += stack.remove(stack.size() - 1);
            }
            stack.add(current);
        }
        return stack;
    }
}