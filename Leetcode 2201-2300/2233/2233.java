// Leetcode 2233: Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/
// Solved on 22nd of November, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Maximizes the product of elements in an array after performing at most `k` increment operations.
     * @param nums The input array of integers.
     * @param k The maximum number of increment operations allowed.
     * @return The maximum possible product modulo 10^9 + 7.
     */
    public int maximumProduct(int[] nums, int k) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int number : nums) {
            priorityQueue.offer(number);
        }

        while (k > 0) {
            int smallest = priorityQueue.poll();
            priorityQueue.offer(smallest + 1);
            k--;
        }

        long result = 1;
        int modulo = 1000000007;

        while (!priorityQueue.isEmpty()) {
            result = (result * priorityQueue.poll()) % modulo;
        }

        return (int) result;
    }
}