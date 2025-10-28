// Leetcode 3066: Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
// Solved on 28th of October, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum number of operations to make all elements in the array
     * greater than or equal to a given threshold `k`.
     * @param nums The input array of integers.
     * @param k The threshold value.
     * @return The minimum number of operations required.
     */
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.add((long) num);
        }

        int operations = 0;

        while (minHeap.size() > 1 && minHeap.peek() < k) {
            long firstSmallest = minHeap.poll();
            long secondSmallest = minHeap.poll();
            
            long newValue = firstSmallest * 2 + secondSmallest;
            
            minHeap.add(newValue);
            operations++;
        }

        return operations;
    }
}