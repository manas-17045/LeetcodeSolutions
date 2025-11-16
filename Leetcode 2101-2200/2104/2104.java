// LLeetcode 2104: Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/
// Solved on 16th of November, 2025
class Solution {
    /**
     * Calculates the sum of ranges of all subarrays. The range of a subarray is the difference between its maximum and minimum element.
     * @param nums The input array of integers.
     * @return The sum of ranges of all subarrays.
     */
    public long subArrayRanges(int[] nums) {
        int n = nums.length;
        int[] prevGreater = new int[n];
        int[] nextGreaterEqual = new int[n];
        int[] prevLess = new int[n];
        int[] nextLessEqual = new int[n];
        int[] stack = new int[n];
        int top = 0;
        for (int i = 0; i < n; i++) {
            while (top > 0 && nums[stack[top - 1]] <= nums[i]) {
                top--;
            }
            prevGreater[i] = top == 0 ? -1 : stack[top - 1];
            stack[top++] = i;
        }
        top = 0;
        for (int i = 0; i < n; i++) {
            while (top > 0 && nums[i] >= nums[stack[top - 1]]) {
                nextGreaterEqual[stack[--top]] = i;
            }
            stack[top++] = i;
        }
        while (top > 0) {
            nextGreaterEqual[stack[--top]] = n;
        }
        top = 0;
        for (int i = 0; i < n; i++) {
            while (top > 0 && nums[stack[top - 1]] >= nums[i]) {
                top--;
            }
            prevLess[i] = top == 0 ? -1 : stack[top - 1];
            stack[top++] = i;
        }
        top = 0;
        for (int i = 0; i < n; i++) {
            while (top > 0 && nums[i] <= nums[stack[top - 1]]) {
                nextLessEqual[stack[--top]] = i;
            }
            stack[top++] = i;
        }
        while (top > 0) {
            nextLessEqual[stack[--top]] = n;
        }
        long totalMax = 0;
        long totalMin = 0;
        for (int i = 0; i < n; i++) {
            long left = i - prevGreater[i];
            long right = nextGreaterEqual[i] - i;
            totalMax += (long) nums[i] * left * right;
            left = i - prevLess[i];
            right = nextLessEqual[i] - i;
            totalMin += (long) nums[i] * left * right;
        }
        return totalMax - totalMin;
    }
}