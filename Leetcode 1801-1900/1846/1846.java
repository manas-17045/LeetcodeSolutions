// Leetcode 1846: Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
// Solved on 28th of June, 2026
class Solution {
    /**
     * Calculates the maximum possible value of an element in the input array after performing
     * the allowed decrementing and rearranging operations.
     * @param arr the array of positive integers to decrease and rearrange
     * @return the maximum possible value of the maximum element after operations
     */
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        int n = arr.length;
        int[] counts = new int[n + 1];
        for (int num : arr) {
            counts[Math.min(num, n)]++;
        }
        int miss = 0;
        for (int i = 1; i <= n; i++) {
            if (counts[i] == 0) {
                miss++;
            } else {
                miss = Math.max(0, miss - (counts[i] - 1));
            }
        }
        return n - miss;
    }
}