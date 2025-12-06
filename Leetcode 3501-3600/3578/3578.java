// Leetcode 3578: Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/
// Solved on 6th of December, 2025
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    /**
     * Counts the number of partitions of the input array `nums` such that the difference between the maximum and minimum
     * element in each partition is at most `k`.
     * @param nums The input array of integers.
     * @param k The maximum allowed difference between the maximum and minimum element in a partition.
     * @return The number of valid partitions, modulo 1_000_000_007.
     */
    public int countPartitions(int[] nums, int k) {
        int n = nums.length;
        int mod = 1_000_000_007;
        
        int[] dpSum = new int[n + 1];
        dpSum[0] = 1;
        
        Deque<Integer> minQ = new ArrayDeque<>();
        Deque<Integer> maxQ = new ArrayDeque<>();
        int left = 0;
        
        for (int i = 0; i < n; i++) {
            while (!minQ.isEmpty() && nums[minQ.peekLast()] >= nums[i]) {
                minQ.pollLast();
            }
            minQ.offerLast(i);
            
            while (!maxQ.isEmpty() && nums[maxQ.peekLast()] <= nums[i]) {
                maxQ.pollLast();
            }
            maxQ.offerLast(i);
            
            while (nums[maxQ.peekFirst()] - nums[minQ.peekFirst()] > k) {
                left++;
                if (minQ.peekFirst() < left) {
                    minQ.pollFirst();
                }
                if (maxQ.peekFirst() < left) {
                    maxQ.pollFirst();
                }
            }
            
            int count = dpSum[i];
            if (left > 0) {
                count = (count - dpSum[left - 1] + mod) % mod;
            }
            
            dpSum[i + 1] = (dpSum[i] + count) % mod;
        }
        
        return (dpSum[n] - dpSum[n - 1] + mod) % mod;
    }
}